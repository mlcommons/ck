"""Convert weights from a gpt-j-6b model to a pax one.

Usage:

# Install the latest main branch of huggingface/transformers
pip3 install git+https://github.com/huggingface/transformers

# Get a checkpiont from the GPTJ family
https://huggingface.co/EleutherAI/gpt-j-6b

This points to
https://github.com/huggingface/transformers/blob/v4.30.2/src/transformers/models/gptj/modeling_flax_gptj.py
and in the default config, use_parallel_residual is true

# Example cmd:
python3 -m convert_gptj_ckpt --base EleutherAI/gpt-j-6b --pax pax_3b
"""
import argparse
import jax
from jax.experimental import pjit
import numpy as np
from paxml import checkpoints
from paxml import train_states
from praxis import py_utils
from transformers import AutoModelForCausalLM

# 6B example
num_layers = 28
num_heads = 16
dims_per_head = 256
vocab = 50401
num_gpus = 1


def convert(base_model_path, pax_model_path):
  """Convert from gpt-j-6b to pax."""
  print(f'Loading the base model from {base_model_path}')

  base = AutoModelForCausalLM.from_pretrained(
      base_model_path, low_cpu_mem_usage=True
  )
  for key, value in base.state_dict().items():
    print('%s %s' % (key, value.data.numpy().shape))

  jax_weights = {
      'lm': {
          'embedding_lookup': {
              'emb_var': base.state_dict()[
                  'transformer.wte.weight'
              ].data.numpy()[:vocab, :]
          },
          'softmax': {
              'logits_ffn': {
                  'linear': {
                      'w': (
                          base.state_dict()['lm_head.weight']
                          .data.numpy()
                          .transpose()[:, :vocab]
                      ),
                  },
                  'bias': {'b': base.state_dict()['lm_head.bias'].data.numpy()},
              }
          },
          'final_ln': {
              'scale': base.state_dict()[
                  'transformer.ln_f.weight'
              ].data.numpy(),
              'bias': base.state_dict()['transformer.ln_f.bias'].data.numpy(),
          },
          'transformer': {},
      }
  }

  for layer_idx in range(num_layers):
    query = base.state_dict()[
        'transformer.h.%d.attn.q_proj.weight' % layer_idx
    ].data.numpy()
    key = base.state_dict()[
        'transformer.h.%d.attn.k_proj.weight' % layer_idx
    ].data.numpy()
    value = base.state_dict()[
        'transformer.h.%d.attn.v_proj.weight' % layer_idx
    ].data.numpy()
    wc = np.stack((query, key, value))
    wc = np.reshape(
        wc, [3, num_heads, dims_per_head, num_heads * dims_per_head]
    )
    wc = np.transpose(wc, (0, 3, 1, 2))

    w_post = base.state_dict()[
        'transformer.h.%d.attn.out_proj.weight' % layer_idx
    ].data.numpy()
    w_post = np.reshape(
        w_post, [num_heads * dims_per_head, num_heads, dims_per_head]
    )
    layer_weight = {
        'self_attention': {
            'combined_qkv': {
                'w': wc,
            },
            'post': {
                'w': w_post,
            },
        },
        'ff_layer': {
            'ffn_layer1': {
                'linear': {
                    'w': (
                        base.state_dict()[
                            'transformer.h.%d.mlp.fc_in.weight' % layer_idx
                        ]
                        .data.numpy()
                        .transpose()
                    ),
                },
                'bias': {
                    'b': base.state_dict()[
                        'transformer.h.%d.mlp.fc_in.bias' % layer_idx
                    ].data.numpy(),
                },
            },
            'ffn_layer2': {
                'linear': {
                    'w': (
                        base.state_dict()[
                            'transformer.h.%d.mlp.fc_out.weight' % layer_idx
                        ]
                        .data.numpy()
                        .transpose()
                    ),
                },
                'bias': {
                    'b': base.state_dict()[
                        'transformer.h.%d.mlp.fc_out.bias' % layer_idx
                    ].data.numpy(),
                },
            },
        },
        'layer_norm': {
            'scale': base.state_dict()[
                'transformer.h.%d.ln_1.weight' % layer_idx
            ].data.numpy(),
            'bias': base.state_dict()[
                'transformer.h.%d.ln_1.bias' % layer_idx
            ].data.numpy(),
        },
    }
    jax_weights['lm']['transformer']['x_layers_%d' % layer_idx] = layer_weight

  print(f'Saving the pax model to {pax_model_path}')
  jax_states = train_states.TrainState(
      step=0, mdl_vars={'params': jax_weights}, opt_states={}
  )
  device_mesh = py_utils.create_device_mesh([1, 1, num_gpus])
  global_mesh = jax.sharding.Mesh(device_mesh, ['replica', 'data_mdl2', 'mdl'])

  # Identity pjit is needed to output a GDA model_states.
  def identity(x):
    return x

  pjitted_identity = pjit.pjit(identity, in_shardings=None, out_shardings=None)
  with global_mesh:
    jax_states_gda = pjitted_identity(jax_states)

  checkpoints.save_checkpoint(
      jax_states_gda,
      pax_model_path,
      checkpoint_type=checkpoints.CheckpointType.GDA,
  )
  print('done')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--base-model-path', type=str, required=True)
  parser.add_argument('--pax-model-path', type=str, required=True)
  args = parser.parse_args()

  convert(args.base_model_path, args.pax_model_path)
