#!/bin/bash

${CM_SUDO} groupadd -g 1111 ckuser
${CM_SUDO} useradd -u 2222 -g ckuser --create-home --shell /bin/bash ckuser
${CM_SUDO} echo "ckuser:ckuser" | chpasswd
${CM_SUDO} adduser ckuser sudo
${CM_SUDO} echo "ckuser   ALL=(ALL)  NOPASSWD:ALL" >> /etc/sudoers
