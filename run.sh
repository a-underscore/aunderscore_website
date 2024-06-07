#!/bin/sh

export PYTHONOPTIMIZE=2

gunicorn -c gunicorn.conf.py
