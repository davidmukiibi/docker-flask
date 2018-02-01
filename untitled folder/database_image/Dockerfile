
##################################################################################################
# this is the postgres base image built on top of the official postgres image by from docker hub #
##################################################################################################

FROM postgres

COPY . /

RUN echo `pwd`

RUN apt-get update && apt-get install -y python-setuptools curl && curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && python -m pip install --upgrade pip && \
pip install --upgrade setuptools && pip install -r requirements.txt && apt-get install -y software-properties-common postgresql-9.3 postgresql-client-9.3 \
postgresql-contrib-9.3 gcc libpq-dev build-essential sudo python-psycopg2 python-dev

