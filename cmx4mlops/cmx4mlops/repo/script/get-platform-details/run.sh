#!/bin/bash

OUTPUT_FILE="$CM_PLATFORM_DETAILS_FILE_PATH"
#set -e
#echo $OUTPUT_FILE
echo "WARNING: sudo permission is needed for some of the below commands"

echo "Platform Details" > $OUTPUT_FILE
echo "" >> $OUTPUT_FILE
echo "------------------------------------------------------------" >> $OUTPUT_FILE
echo "1. uname -a" >> $OUTPUT_FILE
eval "uname -a" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "2. w" >> $OUTPUT_FILE
eval "w" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "3. Username" >> $OUTPUT_FILE
eval "whoami" >> $OUTPUT_FILE
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "4. ulimit -a" >> $OUTPUT_FILE
eval "ulimit -a" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "5. sysinfo process ancestry" >> $OUTPUT_FILE
eval "pstree" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "6. /proc/cpuinfo" >> $OUTPUT_FILE
eval "cat /proc/cpuinfo" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "7. lscpu" >> $OUTPUT_FILE
eval "lscpu" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "8. numactl --hardware" >> $OUTPUT_FILE
if [[ ${CM_SUDO_USER} == "yes" ]]; then
    echo "${CM_SUDO} numactl --hardware"
    eval "${CM_SUDO} numactl --hardware" >> $OUTPUT_FILE
    test $? -eq 0 || exit $?
else
    echo "Requires SUDO permission" >> $OUTPUT_FILE
fi
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "9. /proc/meminfo" >> $OUTPUT_FILE
eval "cat /proc/meminfo" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "10. who -r" >> $OUTPUT_FILE
eval "who -r" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "11. Systemd service manager version" >> $OUTPUT_FILE
eval "systemctl --version | head -n 1" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "12. Services, from systemctl list-unit-files" >> $OUTPUT_FILE
eval "systemctl list-unit-files" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "13. Linux kernel boot-time arguments, from /proc/cmdline" >> $OUTPUT_FILE
eval "cat /proc/cmdline" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "14. cpupower frequency-info" >> $OUTPUT_FILE
eval "cpupower frequency-info" >> $OUTPUT_FILE
test $? -eq 0 || echo "FAILED: cpupower frequency-info" >> $OUTPUT_FILE
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "15. sysctl" >> $OUTPUT_FILE
if [[ ${CM_SUDO_USER} == "yes" ]]; then
    echo "${CM_SUDO} sysctl -a"
    eval "${CM_SUDO} sysctl -a" >> $OUTPUT_FILE
    test $? -eq 0 || exit $?
else
    echo "Requires SUDO permission" >> $OUTPUT_FILE
fi
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "16. /sys/kernel/mm/transparent_hugepage" >> $OUTPUT_FILE
eval "cat /sys/kernel/mm/transparent_hugepage/enabled" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "17. /sys/kernel/mm/transparent_hugepage/khugepaged" >> $OUTPUT_FILE
eval "cat /sys/kernel/mm/transparent_hugepage/khugepaged/defrag" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "18. OS release" >> $OUTPUT_FILE
eval "cat /etc/os-release" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "19. Disk information" >> $OUTPUT_FILE
eval "lsblk" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "20. /sys/devices/virtual/dmi/id" >> $OUTPUT_FILE
eval "ls /sys/devices/virtual/dmi/id" >> $OUTPUT_FILE
test $? -eq 0 || exit $?
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "21. dmidecode" >> $OUTPUT_FILE
if [[ ${CM_SUDO_USER} == "yes" ]]; then
    eval "${CM_SUDO} dmidecode" >> $OUTPUT_FILE
    test $? -eq 0 || echo "FAILED: dmidecode" >> $OUTPUT_FILE
else
    echo "Requires SUDO permission" >> $OUTPUT_FILE
fi
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "22. BIOS" >> $OUTPUT_FILE
if [[ ${CM_SUDO_USER} == "yes" ]]; then
    eval "${CM_SUDO} dmidecode -t bios" >> $OUTPUT_FILE
    test $? -eq 0 || echo "FAILED: dmidecode -t bios" >> $OUTPUT_FILE
else
    echo "Requires SUDO permission" >> $OUTPUT_FILE
fi
echo "------------------------------------------------------------" >> $OUTPUT_FILE

echo "System information has been saved to $OUTPUT_FILE"
