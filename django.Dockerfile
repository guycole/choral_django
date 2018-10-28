#
FROM python:3.7
#
ENV DJANGO_ENV dev
#ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#
RUN apt-get update 
# && apt-get install -y python3 python3-pip 
#RUN pip3 install --upgrade pip
#
WORKDIR /choral
ADD requirements.txt /choral/
RUN pip install -r requirements.txt
#
#ADD choral /choral/
#
#CMD python manage.py runserver
#
