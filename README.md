Coffee monitor
==============

This server is designed to run on a Raspberry pi to monitor the coffee levels.

Installation
------------

The required packages:

* flask
* picamera
* gunicorn

are all listed in `requirements.txt` and can be installed (preferably into a virtualenv) via

``` bash
pip install -r requirements.txt
```

Running
-------

To start the server, run:

``` bash
gunicorn -b unix:/tmp/gunicorn.sock app:app
```

Then configure nginx to bind to the same socket, for example

``` nginx
upstream webcam_server {
    server unix:/tmp/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;
    server_name raspberrypi;

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;

        proxy_pass http://webcam_server;
    }
}
```
