FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive

ADD . /src
WORKDIR /src

RUN echo ${PWD}

RUN apt-get update
RUN apt-get install -y \
  git \
  sudo

RUN sudo apt-get install -y  \
         apt-transport-https \
         ca-certificates \
         curl \
         software-properties-common

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
RUN sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable edge"

RUN sudo apt-get remove docker docker-engine docker.io
RUN sudo apt-get update
RUN sudo apt-get install -y docker-ce

RUN echo ${PWD}

RUN sudo git clone https://github.com/marcelduran/webpagetest-api/

RUN echo ${PWD}

WORKDIR /src/webpagetest-api

RUN echo ${PWD}

RUN sudo docker build -t wpt-api-built-image .

COPY . /src

WORKDIR /src

RUN sudo docker run -t wpt-api-built-image test
