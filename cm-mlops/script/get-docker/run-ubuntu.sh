#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
sudo apt-get update
cmd="sudo apt-get install -y ca-certificates curl gnupg"
echo "$cmd"
eval "$cmd"

test $? -eq 0 || exit $?

if [[ ! -d /etc/apt/keyrings ]]; then
  sudo install -m 0755 -d /etc/apt/keyrings
fi
test $? -eq 0 || exit $?

cmd="curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg"
echo "$cmd"
eval "$cmd"

sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
cmd="sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin"
echo "$cmd"
eval "$cmd"
test $? -eq 0 || exit $?

if [[ -z $USER ]]; then
  USER=`whoami`
fi

cmd="sudo usermod -aG docker $USER"
echo "$cmd"
eval "$cmd"
test $? -eq 0 || exit $?
#exec newgrp docker
#sudo su - $USER

