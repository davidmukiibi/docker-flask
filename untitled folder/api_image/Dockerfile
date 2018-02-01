
#####################################################################################
# this is the base image for my API built on top of the python 2.X image by docker. #
#####################################################################################

FROM python:2

RUN mkdir -p /app/amitytheapp

COPY . /app/amitytheapp

WORKDIR /app/amitytheapp/bucketlist

RUN apt-get update && apt-get install -y sudo curl python-setuptools python-dev && apt-get install -y build-essential apt-utils \
&& curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && python -m pip install --upgrade pip && apt-get install -y libpq-dev \
&& pip install --upgrade setuptools && pip install -r requirements.txt
