# Add the amdgpu module repository for RHEL
repo1="[amdgpu]
name=amdgpu
baseurl=https://repo.radeon.com/amdgpu/${CM_VERSION}/rhel/${CM_HOST_OS_VERSION}/main/x86_64
enabled=1
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
"
echo "${repo1}" | sudo tee /etc/yum.repos.d/amdgpu.repo

# Add the rocm repository for RHEL
mainversion="${CM_HOST_OS_VERSION%%.*}"
repo2="[rocm]
name=rocm
baseurl=https://repo.radeon.com/rocm/rhel${mainversion}/latest/main
enabled=1
priority=50
gpgcheck=1
gpgkey=https://repo.radeon.com/rocm/rocm.gpg.key
"
echo "${repo2}" | sudo tee /etc/yum.repos.d/rocm.repo

sudo yum clean all

sudo yum install amdgpu-dkms

sudo yum install rocm-hip-libraries
