#!/usr/bin/env bash
sudo gunicorn -c ../etc/gunicorn_django.conf ask.wsgi:application
