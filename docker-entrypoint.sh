#!/bin/bash
#
python3 manage.py makemigrations
python3 manage.py migrate
#
python3 manage.py collectstatic --clear --noinput
python3 manage.py collectstatic --noinput
#
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &
#
echo starting gunicorn.
#
exec gunicorn choral.wsgi:application \
    --name choral \
    --bind unix:gunicorn.sock \
    --workers 3 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log & 
#
echo starting nginx 
exec service nginx start
#
