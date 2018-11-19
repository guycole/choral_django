#
FROM python:3.7
#
ENV DJANGO_ENV dev
#ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#
WORKDIR /choral
#
RUN pip install --upgrade pip
#
ADD requirements.txt /choral
RUN pip install -r requirements.txt
#
COPY choral /choral/
#
EXPOSE 8000
#
CMD ["python", "manage.py", "runserver"]
#