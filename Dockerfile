# parent image
FROM python:3.7-alpine

# set working dir as app
WORKDIR /app

# copy project to /app dir
COPY . /app

# install prerequisite packages for using postgres database
RUN apk update && \
    rm -rf /var/cache/apk/*

# set app to env
ENV KODONA_ENV dev

# install python dependencies
RUN pip3 install -r requirements.txt

# expose port for access
EXPOSE 5000:5000

ENTRYPOINT [ "python3", "manage.py", "runserver"]