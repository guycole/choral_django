#
FROM ubuntu:16.04
#
#ENV DJANGO_ENV dev
ENV DJANGO_ENV prod
ENV DJANGO_SECRET 000a0ec7-fe72-4e3d-82e4-cea4c7b77cf3
#ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip virtualenv
RUN apt-get install -y vim
RUN apt-get install -y nginx
#
RUN pip3 install --upgrade pip
#
RUN mkdir /static 
RUN mkdir /srv/logs
#
WORKDIR /srv/choral
#
ADD requirements.txt /srv/choral
RUN pip3 install -r requirements.txt
#
COPY choral /srv/choral/
#
COPY ./docker-entrypoint.sh /srv/choral
COPY ./django_nginx.conf /etc/nginx/sites-available/
#
RUN ln -s /etc/nginx/sites-available/django_nginx.conf /etc/nginx/sites-enabled/
#
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
#
EXPOSE 8000
#
ENTRYPOINT ["/srv/choral/docker-entrypoint.sh"]
#
