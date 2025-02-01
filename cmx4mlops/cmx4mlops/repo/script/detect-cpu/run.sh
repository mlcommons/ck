#!/bin/bash

# Function to extract a field from /proc/cpuinfo
extract_field() {
  local key="$1"
  local default="$2"
  # Use awk to find the first occurrence and extract the value
  local value=$(awk -F: -v key="$key" '$1 ~ key {print $2; exit}' /proc/cpuinfo | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

  # Check if value is empty and assign default if needed
  echo "${value:-$default}"
}

if [[ ${CM_HOST_OS_FLAVOR} == "macos" ]]; then
    sysctl -a | grep hw > tmp-lscpu.out
else
    lscpu > tmp-lscpu.out
    memory_capacity=`free -h --si | grep Mem: | tr -s ' ' | cut -d' ' -f2`
    echo "CM_HOST_MEMORY_CAPACITY=$memory_capacity">>tmp-run-env.out
    disk_capacity=`df -h --total -l |grep total |tr -s ' '|cut -d' ' -f2`
    echo "CM_HOST_DISK_CAPACITY=$disk_capacity">>tmp-run-env.out

    # extract cpu information which are not there in lscpu
    CM_HOST_CPU_WRITE_PROTECT_SUPPORT=$(extract_field "wp" "Not Found")
    CM_HOST_CPU_MICROCODE=$(extract_field "microcode" "Not Found")
    CM_HOST_CPU_FPU_SUPPORT=$(extract_field "fpu" "Not Found")
    CM_HOST_CPU_FPU_EXCEPTION_SUPPORT=$(extract_field "fpu_exception" "Not Found")
    CM_HOST_CPU_BUGS=$(extract_field "bugs" "Not Found")
    CM_HOST_CPU_TLB_SIZE=$(extract_field "TLB size" "Not Found")
    CM_HOST_CPU_CFLUSH_SIZE=$(extract_field "clflush size" "Not Found")
    CM_HOST_CACHE_ALIGNMENT_SIZE=$(extract_field "cache_alignment" "Not Found")
    CM_HOST_POWER_MANAGEMENT=$(extract_field "power management" "Not Found")

    # Write results to a file
    {
      echo "CM_HOST_CPU_WRITE_PROTECT_SUPPORT=$CM_HOST_CPU_WRITE_PROTECT_SUPPORT"
      echo "CM_HOST_CPU_MICROCODE=$CM_HOST_CPU_MICROCODE"
      echo "CM_HOST_CPU_FPU_SUPPORT=$CM_HOST_CPU_FPU_SUPPORT"
      echo "CM_HOST_CPU_FPU_EXCEPTION_SUPPORT=$CM_HOST_CPU_FPU_EXCEPTION_SUPPORT"
      echo "CM_HOST_CPU_BUGS=$CM_HOST_CPU_BUGS"
      echo "CM_HOST_CPU_TLB_SIZE=$CM_HOST_CPU_TLB_SIZE"
      echo "CM_HOST_CPU_CFLUSH_SIZE=$CM_HOST_CPU_CFLUSH_SIZE"
      echo "CM_HOST_CACHE_ALIGNMENT_SIZE=$CM_HOST_CACHE_ALIGNMENT_SIZE"
      echo "CM_HOST_POWER_MANAGEMENT=$CM_HOST_POWER_MANAGEMENT"
    } >> tmp-run-env.out
fi


