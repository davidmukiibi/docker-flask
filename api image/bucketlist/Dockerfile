
##################################################################################################
# the API applciation image built on top of the custom API base image built using python 2 image #
##################################################################################################

FROM mukiibi:api_base_image

ENV DEV_SECRET_KEY=thisisit
ENV APP_SETTING=development
ENV APP_SETTING=development
ENV PGPASSWORD=docker
ENV DATABASE_URL=postgresql://postgres@localhost:5432/dockerdb

COPY . /app/amitytheapp

WORKDIR /app/amitytheapp

EXPOSE 5000

CMD ["python", "run.py"]
