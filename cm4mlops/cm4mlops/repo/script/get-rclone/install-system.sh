#!/bin/bash
sudo -v ; curl -k https://rclone.org/install.sh | sudo bash
test $? -eq 0 || exit 1
