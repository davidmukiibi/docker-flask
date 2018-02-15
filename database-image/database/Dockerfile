FROM postgres

# copy createdb.sql file to the postgres /docker-entrypoint-initdb.d folder
# to run on iitial database start up
ADD createdb.sql /docker-entrypoint-initdb.d

# expose default postgres server port
EXPOSE 5432


