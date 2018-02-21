FROM ubuntu:artful

ENV DEBIAN_FRONTEND=noninteractive

# RUN mkdir /opt

RUN apt-get update && apt-get install -y sudo

RUN sudo apt-get remove docker docker-engine docker.io

RUN sudo apt-get update
RUN sudo apt-get install -y apt-transport-https \
  ca-certificates \
  curl \
  software-properties-common

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
RUN sudo apt-key fingerprint 0EBFCD88

RUN sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable edge"

RUN sudo apt-get update
RUN sudo apt-get install -y docker-ce

# RUN sudo docker run -v /var/run/docker.sock:/var/run/docker.sock -d --name firefoxtesteng/webpagetest-api test
RUN sudo docker run --privileged=true -w /mnt/foo -v $PWD/foo:/mnt/foo -t --rm firefoxtesteng/webpagetest-api test

RUN sudo docker hello-world

RUN sudo docker run --privileged=true --rm -t \
  WEBPAGETEST_SERVER=https://${WEB_PAGE_TEST}@wpt-api.stage.mozaws.net/ \
  firefoxtesteng/webpagetest-api test 'https://latest.dev.lcip.org/?service=sync&entrypoint=firstrun&context=fx_desktop_v3' \
  -l 'us-east-1:Firefox' -r 9 --first --poll --reporter json > 'fxa-firstrunpage.json'

# Eventually, I'd like to do the following (building from source, rather than pulling down):
#
# RUN git clone https://github.com/stephendonner/webpagetest-api /src/wpt-api
# ADD . /src/wpt-api
# WORKDIR /src/wpt-api
# RUN docker build -t webpagetest-api .

CMD docker run --rm -t -v /home/jenkins/workspace/wpt.fxa-homepage:/mnt/workspace -w \
/mnt/workspace --entrypoint /usr/src/app/bin/webpagetest -e \
WEBPAGETEST_SERVER=https://${WEB_PAGE_TEST}@wpt-api.stage.mozaws.net/ \
firefoxtesteng/webpagetest-api test 'https://latest.dev.lcip.org/?service=sync&entrypoint=firstrun&context=fx_desktop_v3' \
-l 'us-east-1:Firefox' -r 9 --first --poll --reporter json > 'fxa-firstrunpage.json'
