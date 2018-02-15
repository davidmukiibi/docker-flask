FROM python:2.7

RUN apt-get update -yqq \
  && apt-get install -yqq --no-install-recommends apt-utils\
    netcat \
  && apt-get -q clean

# creating folder /app
RUN mkdir /app

# copying all contents of the dockerfile folder to folder /app
COPY . /app

# specifying the preffered working directory
WORKDIR /app/bucketlist

# making the script executable
RUN chmod +x start_postgres.sh

# installing API dependencies
RUN pip install -r requirements.txt

# exposing the flask application default port
EXPOSE 5000

# run server
CMD ["./start_postgres.sh"]