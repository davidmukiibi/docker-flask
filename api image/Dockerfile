
######################################################################################
# bucketlist application API base image built on top of the python2 docker hub image #
######################################################################################


FROM python:2

ENV DEV_SECRET_KEY=thisisit
ENV APP_SETTING=development
ENV APP_SETTING=development
ENV PGPASSWORD=docker
ENV DATABASE_URL=postgresql://postgres@localhost:5432/dockerdb

RUN mkdir -p /app/amitytheapp

COPY . /app/amitytheapp

WORKDIR /app/amitytheapp/bucketlist

RUN apt-get update && apt-get install -y sudo curl python-setuptools python-dev && apt-get install -y build-essential apt-utils \
&& curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && python -m pip install --upgrade pip && apt-get install -y libpq-dev \
&& pip install --upgrade setuptools

RUN pip install -r requirements.txt

EXPOSE 5000