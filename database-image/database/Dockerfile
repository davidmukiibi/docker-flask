# this tells the docker daemon(read docker) to build an image on top of 
# a postgres image of any version. the postgres image is the base image for the current image we build with this file
FROM postgres

# this adds the createdb.sql file to the postgres server folder /docker-entrypoint-initdb.d
# to run on initial database server start up. on start up, all .sql, .sh files in this folder
# are run, which makes it the best place to create a database we shall be using.
ADD createdb.sql /docker-entrypoint-initdb.d

# declare the default postgres server port
EXPOSE 5432


