# this tells docker to build this image on top if python version 2.7.*
FROM python:2.7

# this is installing environment dependencies
RUN apt-get update -yqq \
  && apt-get install -yqq --no-install-recommends apt-utils\
    netcat \
  && apt-get -q clean

# here we are creating a folder named /app
RUN mkdir /app

# here we are copying all contents of the current folder where the dockerfile resides to the folder /app
COPY . /app

# this is changing the current working directory to /app/bucketlist
# this is required since it is that folder where we find the requirements.txt
# file that essentially is a file that contains the application API dependencies
WORKDIR /app/bucketlist

# making the script executable
RUN chmod +x start_postgres.sh

# installing API dependencies
RUN pip install -r requirements.txt

# exposing the flask application default port
EXPOSE 5000

# this will execute this bash script named start_postgres.sh when a container is
# created from this image
CMD ["./start_postgres.sh"]