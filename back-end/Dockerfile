FROM debian:jessie AS BACK_DFC

LABEL maintainer="Courtel Eliot"
LABEL maintainermail="eliot.courtel@wanadoo.fr"

RUN apt-get update && apt-get install curl -y 
RUN cd ~ && curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install nodejs build-essential -y
RUN npm install -g pm2
RUN apt-get install python3 python3-pip -y --no-install-recommends
RUN apt-get install git -y --no-install-recommends
RUN pip3 install requests bottle uuid
RUN easy_install3 -U pip 
RUN pip install google-cloud-language
RUN apt-get install openssh-client -y --no-install-recommends
RUN mkdir /home/api
RUN apt-get install nano -y --no-install-recommends
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

ENTRYPOINT cd /home/api/ && cp /home/api/secret.json /home/api/secret_copy.json && \
	   if [ "$PROD" -eq 1 ]; then mkdir prod; cd prod; git clone --quiet https://github.com/SCcagg5/DialogFlowSentimentAnalyser > /dev/null; fi && \
	   cd ./DialogFlowSentimentAnalyser/back-end/src && pm2 start --interpreter python3 server.py --watch > /dev/null & > /dev/null; \
	   /bin/bash
