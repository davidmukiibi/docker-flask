
##############################################################################
# this is the postgres database image built on top of my postgres base image #
##############################################################################

FROM mukiibi:postgres_base_image

ENV DEV_SECRET_KEY=thisisit
ENV APP_SETTING=development
ENV PGPASSWORD=docker
ENV DATABASE_URL=postgresql://postgres@localhost:5432/dockerdb

RUN mkdir -p /app/amity

# RUN su postgres

COPY . /app/amity

WORKDIR /app/amity/bucketlist  

RUN sudo chown -R postgres:postgres /app/amity

RUN chmod +x ../postgres_migrations.sh

USER postgres

RUN [".././postgres_migrations.sh"]

# # Adjust PostgreSQL configuration so that remote connections to the
# # database are possible.
# RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf

# # And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``
# RUN mkdir -p /etc/postgresql/9.3/main/ && touch /etc/postgresql/9.3/main/postgresql.conf

# RUN echo "listen_addresses='0.0.0.0'" >> /etc/postgresql/9.3/main/postgresql.conf

EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]


# CMD ["pg_ctl -D /var/lib/postgresql/data -l logfile start"]

CMD ["pg_ctl -D /var/lib/postgresql/data -l logfile start"]

# CMD ["pg_ctl -D DATA_DIRECTORY -l logfile start"]



# Set the default command to run when starting the container
# CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]