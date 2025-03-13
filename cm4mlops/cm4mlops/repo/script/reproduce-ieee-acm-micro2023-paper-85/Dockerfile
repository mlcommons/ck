#Bootstrap: docker
From ubuntu:20.04

#%post
    RUN mkdir /root/artifact_evaluation
    RUN apt-get -y clean
    RUN apt-get -y update
	RUN apt-get -y install python3 build-essential
	RUN apt-get -y install git 
	RUN apt-get -y install vim pip 
    RUN pip install numpy
	WORKDIR /root/artifact_evaluation
    RUN git clone https://github.com/lchangxii/sampled-mgpu-sim.git
    RUN git clone https://github.com/lchangxii/akita.git
    RUN git clone https://github.com/lchangxii/dnn.git
	RUN apt-get -y install wget
    RUN wget https://go.dev/dl/go1.20.1.linux-amd64.tar.gz
    RUN tar -xvzf go1.20.1.linux-amd64.tar.gz
    ENV PATH="/root/artifact_evaluation/go/bin:$PATH"
    ENV HOME /root
    RUN git clone https://github.com/lchangxii/micro2023_figures.git
    RUN pip install pandas
    RUN pip install matplotlib
    RUN pip install openpyxl
#%environment
#export PATH=/opt/riscv/:$PATH


