---
layout: default
title: Execute app locally
nav_order: 4
---

# Execute app locally

In the root folder of the repository there is a simple python application that will be used for this exercise.
It is not intended to be a template for python applications or to be used in production, it is simply something that can be executed within a pod.

It's a simple flask server that serves a static html page and exposes one endpoint `/getsomething`

## Run locally

In order to execute the app, you must have python installed on your system.
The code was tested on python `v 3.8.10`.

Install the dependencies

``` bash
pip install -r requirements.txt
```

start the server

``` bash
python run.py
```

You should see a message like the following

``` bash
$ python run.py 
 * Serving Flask app 'frontend-flask' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:8080
 * Running on http://192.168.1.7:8080 (Press CTRL+C to quit)
 ```

> ❗️ In a real scenario, you want to build and serve the flask app with a different mean, some extra details in the [documentation](https://flask.palletsprojects.com/en/2.1.x/deploying/)
