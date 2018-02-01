
FROM postgres

COPY . /appfiles

WORKDIR /appfiles

RUN apt-get update && apt-get install -y software-properties-common postgresql-9.3 postgresql-client-9.3 \
postgresql-contrib-9.3 curl gcc libpq-dev build-essential sudo python-psycopg2 python-setuptools python-dev && \
curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && python -m pip install --upgrade pip && \
pip install --upgrade setuptools && pip install -r requirements.txt
