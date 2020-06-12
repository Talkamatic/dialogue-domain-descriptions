FROM python:3.7-slim

RUN apt-get update -qq && apt-get install -y --no-install-recommends \
  build-essential \
  git-core \
  openssh-client && \
  apt-get upgrade -y && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade pip

COPY ./requirements.txt ./
RUN pip --no-cache-dir install -r requirements.txt && rm -f requirements.txt
