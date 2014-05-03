#!/bin/bash

echo 'hello-boilerplate package installed'.

sudo ln -s /etc/nginx/sites-available/hello-conf /etc/nginx/sites-enabled/hello-conf
rm -rf /etc/nginx/sites-enabled/default

service supervisor restart
service nginx restart
