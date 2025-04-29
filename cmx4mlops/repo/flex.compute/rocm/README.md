# 20241111: Grigori's ROCm and AMD MI300X tests

* To solve ```RuntimeError: No HIP GPUs are available```, we need
  to add current user to render and video groups:

  https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/prerequisites.html

  ```bash
  sudo usermod -a -G render,video $LOGNAME
  ```
* ROCm translates CUDA codes. We need to use "cuda" device in PyTorch to use ROCm.

* We can test that ROCm is supported in PyTorch via
  ```torch.__version__``` and ```torch.cuda.is_available()```

```bash
ft "use sys tool" --name=pip_torch --compute_tags=rocm --renew --j --v
```

TBD: FT currently forces installation of PyTorch with ROCm v6.2.
