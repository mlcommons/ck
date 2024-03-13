#!/bin/bash

if [[ ! -f /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg ]]; then
  cmd="curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg"
  echo "$cmd"
  eval "$cmd"
fi

cmd="curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
  && \
    sudo apt-get update"
echo "$cmd"
eval "$cmd"
test $? -eq 0 || exit $?

cmd="sudo apt-get install -y nvidia-container-toolkit"
echo "$cmd"
eval "$cmd"
test $? -eq 0 || exit $?

cmd="sudo nvidia-ctk runtime configure --runtime=docker"
echo "$cmd"
eval "$cmd"
test $? -eq 0 || exit $?

cmd="sudo systemctl restart docker"
cmd="sudo service docker restart"
echo "$cmd"
eval "$cmd"
test $? -eq 0 || exit $?
