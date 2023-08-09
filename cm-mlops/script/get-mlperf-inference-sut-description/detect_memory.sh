#!/bin/bash

if [[ ${CM_SUDO_USER} == "yes" ]]; then
  sudo dmidecode -t memory > meminfo.out
fi
