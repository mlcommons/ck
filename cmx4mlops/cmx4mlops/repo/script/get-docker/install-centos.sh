sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

cmd="sudo usermod -aG docker $USER"
echo "$cmd"
eval "$cmd"
test $? -eq 0 || exit $?

echo "Please relogin to the shell so that the new group is  effective"
exit 1
#exec newgrp docker
#sudo su - $USER
