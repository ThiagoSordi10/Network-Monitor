FROM ubuntu:16.04
MAINTAINER Thiago Sordi version: 0.4

USER root


#
# Define where things will be installed
#

# Base dir for work is the user directory 
ARG HOME_DIR=/root
# Where to put sources to compile
ARG SRC_DIR=${HOME_DIR}/sources
# Where to put .pcap files
ARG PCAP_DIR=${HOME_DIR}/pcap_files
# Base install dir for binaries
ARG INSTALL_DIR=/usr/local
# Installed Zeek base dir
ARG ZEEK_BASE_DIR=${INSTALL_DIR}/zeek

#
# Create needed base directories
#

RUN mkdir -p ${SRC_DIR}
RUN mkdir -p ${PCAP_DIR}
RUN mkdir -p ${ZEEK_BASE_DIR}

# Update apt sources/ Git, make, gcc..., Special additional components needed for building zeek workspace, CMaken / Install nano, ifconfig to be able to check container ip, ping requests to easily generate # a DNS query
RUN apt-get update; \
    apt-get install -y git build-essential python-dev flex bison libpcap-dev libssl-dev zlib1g-dev flex bison swig cmake; \
    apt-get install -y nano net-tools iputils-ping procps; \
    apt-get clean;


#
# Install sources, build and install Zeek, librdkafka and the Bro-Kafka plugin
#
    
# Download, build and install Zeek 
RUN cd ${SRC_DIR}; \
    git clone --recursive https://github.com/zeek/zeek; \
    cd zeek;  \
    ./configure --prefix=${ZEEK_BASE_DIR}; \
    make; \
    make install; \
    cd ..; \
    git clone https://github.com/edenhill/librdkafka.git; \
    cd librdkafka;  \
    ./configure --prefix=${INSTALL_DIR}; \
    make; \
    make install; \
    cd ..; \
    cd ${SRC_DIR}; \
    git clone https://github.com/apache/metron-bro-plugin-kafka.git; \
    cd metron-bro-plugin-kafka; \
    ./configure --install-root=${ZEEK_BASE_DIR}/lib/zeek/plugins --bro-dist=${SRC_DIR}/zeek --with-librdkafka=${INSTALL_DIR}/lib; \
    make; \
    make install; \
    cd ..; \
    rm -R zeek; \
    rm -R librdkafka; \
    rm -R metron-bro-plugin-kafka;
    


#
# Define environment variables
#

# Zeek
ENV ZEEK_HOME ${ZEEK_BASE_DIR}
# Update path for Zeek binary
ENV PATH="${ZEEK_HOME}/bin:${PATH}"
# Pcap files
ENV PCAP_HOME ${PCAP_DIR}

#
# Copy .pcap files
#

# ssh.pcap comes from https://www.bro.org/bro-workshop-2011/solutions/notices/
# It is used to be able to easily generate a Bro notice (password guessing)
COPY local.zeek $ZEEK_HOME/share/zeek/site
COPY ssh.pcap ${PCAP_DIR}

WORKDIR /root
