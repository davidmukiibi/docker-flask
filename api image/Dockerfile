
######################################################################################
# bucketlist application API base image built on top of the python2 docker hub image #
######################################################################################


FROM python:2.7

# ENV DEV_SECRET_KEY=thisisit
# ENV APP_SETTING=development
# ENV APP_SETTING=development
# ENV PGPASSWORD=docker
# ENV DATABASE_URL=postgresql://postgres:postgres@amity-db:5432/docker

RUN apt-get update -yqq \
  && apt-get install -yqq --no-install-recommends apt-utils\
    netcat \
  && apt-get -q clean


RUN mkdir /app

COPY . /app

WORKDIR /app/bucketlist

RUN chmod +x start_postgres.sh

RUN pip install -r requirements.txt

EXPOSE 5000

# run server
CMD ["./start_postgres.sh"]