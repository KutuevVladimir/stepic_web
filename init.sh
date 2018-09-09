#!/usr/bin/env bash
sudo rm /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
cd ask
sudo bash server_run.sh
#sudo ln -sf /home/box/web/etc/gunicorn_wsgi.conf /etc/gunicorn.d/test-wsgi
#sudo ln -sf /home/box/web/etc/gunicorn_django.conf /etc/gunicorn.d/test-django
#sudo /etc/init.d/gunicorn restart
#sudo gunicorn -c etc/gunicorn_wsgi.conf hello:app

