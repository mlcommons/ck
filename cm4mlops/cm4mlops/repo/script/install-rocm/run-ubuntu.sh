#!/bin/bash
# Make the directory if it doesn't exist yet.
# This location is recommended by the distribution maintainers.
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
# Download the key, convert the signing-key to a full
# keyring required by apt and store in the keyring directory
wget https://repo.radeon.com/rocm/rocm.gpg.key -O - | \
    gpg --dearmor | sudo tee /etc/apt/keyrings/rocm.gpg > /dev/null

ubuntuflavor="jammy"
if [[ ${CM_HOST_OS_VERSION} == "22.04" ]]; then
  ubuntuflavor="jammy"
elif [[ ${CM_HOST_OS_VERSION} == "20.04" ]]; then
  ubuntuflavor="focal"
fi

# Kernel driver repository
deb1="deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/${CM_VERSION}/ubuntu ${ubuntuflavor} main"
echo $deb1 | sudo tee /etc/apt/sources.list.d/amdgpu.list

# ROCm repository
deb2="deb [arch=amd64 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/rocm/apt/debian ${ubuntuflavor} main"
echo $deb2 | sudo tee /etc/apt/sources.list.d/rocm.list

# Prefer packages from the rocm repository over system packages
echo -e 'Package: *\nPin: release o=repo.radeon.com\nPin-Priority: 600' | sudo tee /etc/apt/preferences.d/rocm-pin-600

sudo apt update

sudo apt install amdgpu-dkms

sudo apt install rocm-hip-libraries
