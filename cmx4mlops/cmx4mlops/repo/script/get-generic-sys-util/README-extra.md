Please see [https://docs.mlcommons.org/cm4mlops/scripts/Detection-or-installation-of-tools-and-artifacts/get-generic-sys-util](https://docs.mlcommons.org/cm4mlops/scripts/Detection-or-installation-of-tools-and-artifacts/get-generic-sys-util) for the documentation of this CM script.

# get-generic-sys-util
Below are the specific regexes and the format of output that they are expecting for each command used to check for versions. 

All commands are tested to be working on Ubuntu.

Format:

## Utility name
`regex`

`command to obtain version`

command output

----

## g++-12
`^.*([0-9]+(\\.[0-9]+)+).*`

`g++-9 --version`

g++-9 (Ubuntu 9.5.0-1ubuntu1~22.04) <mark>9.5.0</mark></br>
Copyright (C) 2019 Free Software Foundation, Inc. </br>
This is free software; see the source for copying conditions.  There is NO </br>
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </br>

## g++-11
`^.*([0-9]+(\\.[0-9]+)+).*`

`g++-11 --version`

g++-11 (Ubuntu 11.4.0-1ubuntu1~22.04) <mark>11.4.0 </mark></br>
Copyright (C) 2021 Free Software Foundation, Inc. </br>
This is free software; see the source for copying conditions.  There is NO </br>
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </br>

## g++-12
`^.*([0-9]+(\\.[0-9]+)+).*`

`g++-12 --version`

g++-12 (Ubuntu 12.3.0-1ubuntu1~22.04)  <mark>12.3.0 </mark></br>
Copyright (C) 2022 Free Software Foundation, Inc. </br>
This is free software; see the source for copying conditions.  There is NO </br>
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </br>


## gcc-9
`^.*([0-9]+(\\.[0-9]+)+).*`

`gcc-9 --version`

gcc-9 (Ubuntu 9.5.0-1ubuntu1~22.04) <mark>9.5.0</mark></br>
Copyright (C) 2019 Free Software Foundation, Inc. </br>
This is free software; see the source for copying conditions.  There is NO </br>
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </br>

## gcc-11
`^.*([0-9]+(\\.[0-9]+)+).*`

`gcc-11 --version`

gcc-11 (Ubuntu 11.4.0-1ubuntu1~22.04) <mark>11.4.0 </mark></br>
Copyright (C) 2021 Free Software Foundation, Inc. </br>
This is free software; see the source for copying conditions.  There is NO </br>
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </br>


## libgflags-dev
`([\d.]+)`

`pkg-config --modversion gflags`

2.2.2

## libglog-dev
`([\d.]+)`

`pkg-config --modversion libglog`

0.4.0

## libboost-all-dev
`([0-9]+(\w.[0-9]+)+)`

`dpkg -s libboost-dev | grep 'Version'`

Version: <mark>1.74.0.3</mark>ubuntu7


## libpng-dev
`([\d.]+)`

`pkg-config --modversion libpng`

1.6.37

## libre2-dev
`([\d.]+)`

`pkg-config --modversion libre2`

0.0.0

## libpci-dev
`([\d.]+)`

`pkg-config --modversion libpci`

3.7.0


## libreadline_dev
`([\d.]+)`

`pkg-config --modversion readline`

8.1

## zlib
`([\d.]+)`

`pkg-config --modversion zlib`

1.2.11


## libsqlite3_dev
`([\d.]+)`

`pkg-config --modversion sqlite3`

3.37.2

## libssl_dev
`OpenSSL\s+([\d.]+)`

`openssl version`

<mark>OpenSSL 3.0.2</mark> 15 Mar 2022 (Library: OpenSSL 3.0.2 15 Mar 2022)

## libudev-dev
`([\d.]+)`

`pkg-config --modversion libudev`

249


## libbz2_dev
`Version ([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)`

`bzcat --version`

bzip2, a block-sorting file compressor.  <mark>Version 1.0.8, 13-Jul-2019.</mark>

## libev_dev
dpkg here should be fine as only apt install is supported
`Version ([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)`

`dpkg -s libev-dev | grep 'Version'`

Version: <mark>1:4.33-1 </mark>

## libffi-dev
`([\d.]+)`

`pkg-config --modversion libffi`

3.4.2

## libffi_dev
`([\d.]+)`

`pkg-config --modversion libffi`

3.4.2

## libffi7
`\d\.\d-[0-9]+`

`dpkg -l libffi7 2>/dev/null | grep '^ii' | awk '{print $3}' || rpm -q libffi7 2>/dev/null || pacman -Q libffi7 2>/dev/null`

3.3-5ubuntu1

## libffi8
`\d\.\d\.\d-\d`

`pkg-config --modversion libffi8"`

3.4.2-4

## libgdbm_dev
dpkg here should be fine as only apt install is supported
`dpkg -s libgdbm-dev | grep 'Version'`

`([\d]+\.[\d\.-]+)`

Version: <mark>1.23-1</mark>


## libgmock
`([\d.]+)`

`pkg-config --modversion libgmock`

1.11.0

## liblzma_dev
`[A-Za-z]+\s\d\.\d\.\d`

`xz --version`

xz (XZ Utils) 5.2.5
<mark>liblzma 5.2.5</mark>


## libmpfr_dev
`([\d.]+)`

`pkg-config --modversion mpfr`

`4.1.0`

## libncurses_dev
`([0-9]+(\.[0-9]+)+)`

`ncurses5-config --version`

6.3.20211021



## ninja-build
`([\d.]+)`

`ninja --version`

1.11.1

## md5sha1sum
`md5sum \(GNU coreutils\) ([\d.]+)`

`md5sum --version` or `sha1sum --version`

md5sum (GNU coreutils) 9.5 

sha1sum (GNU coreutils) 9.5


## nlohmann-json3-dev
`([\d.]+)`

`pkg-config --modversion nlohmann_json`

`3.10.5`

## ntpdate
`([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)`

`dpkg -l ntpdate 2>/dev/null | grep ^ii | awk '{print $3}'`

1:<mark>4.2.8p15</mark>+dfsg-1ubuntu2

## nvidia-cuda-toolkit
`release ([\d.]+)`

`nvcc --version`

nvcc: NVIDIA (R) Cuda compiler driver<br />
Copyright (c) 2005-2021 NVIDIA Corporation<br />
Built on Thu_Nov_18_09:45:25_PST_2021 <br />
Cuda compilation tools, <mark>release 11.5</mark>, V11.5.119<br />
Build cuda_11.5.r11.5/compiler.30672275_0<br />


## psmisc
`\(PSmisc\) ([\d.]+)`

`pstree --version`

pstree (PSmisc) 23.4

## rapidjson-dev
`([\d.]+)`

`pkg-config --modversion RapidJSON`

<mark>1.1.0</mark>

## cmake
`cmake version ([\d.]+)`

`cmake --version`

cmake version 3.30.4

## libnuma-dev
`([\d.]+)`

`pkg-config --modversion numa`

2.0.14


## numactl
`([\d.]+)`

`pkg-config --modversion numa`

2.0.14

## wget
`Wget\s*([\d.]+)`

`wget --version`

<mark>GNU Wget 1.21.2 </mark>built on linux-gnu.

## screen
`Screen version ([\d.]+)`

`screen --version`

<mark>Screen version 4.00.020</mark> (FAU) 23-Oct-06

## xz
`xz \(XZ Utils\) ([\d.]+)`

`xz --version`

<mark>xz (XZ Utils) 5.2.5 </mark>
liblzma 5.2.5

## VIM
`VIM - Vi IMproved ([\d.]+`

`vim --version`

<mark>VIM - Vi IMproved 9.0 </mark> (2022 Jun 28, compiled Aug  3 2024 14:50:46)

## rsync
`rsync\s+version\s+([\d.]+)`

`rsync --version`

rsync  version 3.2.7  protocol version 31

## sox
`sox:\s+SoX\s+v([\d.]+)`

`sox --version`

sox:      SoX v14.4.2


## systemd
`systemd ([\d]+)`

`systemctl --version`

<mark>systemd 249</mark> (249.11-0ubuntu3.12)

## tk-dev
Probably fine to use `dpkg` here as only installation supported is for ubuntu

`([0-9]+(\.[0-9]+)+)`

`dpkg -s tk-dev | grep Version`

Version: <mark>8.6.11</mark>+1build2


## transmission
`transmission-daemon ([\d.]+)`

`transmission-daemon --version`

transmission-daemon 3.00 (bb6b5a062e)


## wkhtmltopdf
`wkhtmltopdf ([\d.]+)`

`wkhtmltopdf --version`

wkhtmltopdf 0.12.6

## systemd
`systemd ([\d]+)`

`systemd --version`

<mark>systemd 255</mark> (255.4-1ubuntu8.4)


## dmidecode
`([\d.]+)`

`dmidecode --version`

3.3

## git-lfs
`git-lfs/([\d.]+)`

`git-lfs --version`

<mark>git-lfs/3.4.1</mark> (GitHub; linux arm64; go 1.22.2)

## zlib1g
`([\d.]+)`

`pkg-config --modversion zlib`

1.2.11

## zlib1g_dev
`([\d.]+)`

`pkg-config --modversion zlib`

1.2.11
