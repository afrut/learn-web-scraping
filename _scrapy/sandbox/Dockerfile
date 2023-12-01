FROM ubuntu:mantic-20231011
RUN apt update && \
    apt install build-essential -y && \
    apt install nodejs npm -y && \
    npm install -g scrapoxy
ARG workdir="/scrapoxy"
WORKDIR $workdir