rem https://pytorch.org/get-started/previous-versions

ft "test image-classification pytorch" --v ^
    --state.flow.pip_torch.renew --state.flow.pip_torch.version=2.4.1 ^
    --state.flow.pip_torchvision.renew --state.flow.pip_torchvision.version=0.19.1
