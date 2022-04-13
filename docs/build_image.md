---
layout: default
title: Build container image
nav_order: 5
---

# Build container image

The goal of this step is to create an image of your application.
The main activity here is to create a Dockerfile and use it to build locally the image

## Create Dockerfile

In the root of the project you can find a sample Dockerfile that you can use to build the image.
You can find the full details of the syntax for a Dockerfile [here](https://docs.docker.com/engine/reference/builder/).

The Dockerfile available here is really simple and has a few basic instructions

### FROM

The **FROM** instruction initializes a new build stage and sets the Base Image for subsequent instructions. As such, a valid Dockerfile must start with a **FROM** instruction. The image can be any valid image – it is especially easy to start by pulling an image from the [Public Repositories](https://docs.docker.com/docker-hub/repos/).

``` bash
FROM python:3.8-slim
```

We are using a base image that already comes with python installed (the same version I used to test locally the app)

### COPY

The **COPY** instruction copies new files or directories from `<src>` (first param) and adds them to the filesystem of the container at the path `<dest>`.

``` bash
COPY . /app
```

> 💡 As you would do with files that you do not want to push to git, you can list in the `.dockerignore` the files to exclude from the image.

### WORKDIR

The **WORKDIR** instruction sets the working directory for any **RUN**, **CMD**, **ENTRYPOINT**, **COPY** and **ADD** instructions that follow it in the `Dockerfile`

``` bash
WORKDIR /app
```

### EXPOSE

The **EXPOSE** instruction informs Docker that the container listens on the specified network ports at runtime. You can specify whether the port listens on TCP or UDP, and the default is TCP if the protocol is not specified.

``` bash
EXPOSE 8080/tcp
```

## Build image locally

Open a terminal in the root folder of the project and build the image with the following command

``` bash
docker build -t <image_name>:<image_version> .
```

for podman, the command is almost identical

``` bash
podman build -t <image_name>:<image_version> .
```

> ❗️ Note the trailing `.` as it tells where the `Dockerfile` actually is

example

``` bash
podman build -t kube-lab:1.0 .

STEP 1/6: FROM python:3.8-slim
Resolved "python" as an alias (/etc/containers/registries.conf.d/000-shortnames.conf)
Trying to pull docker.io/library/python:3.8-slim...
Getting image source signatures
Copying blob sha256:d783e1f0a3ebf406d360da14f3534e8d1f0d835a708ec9c80891f3eddca01064
Copying blob sha256:c229119241af7b23b121052a1cae4c03e0a477a72ea6a7f463ad7623ff8f274b
....

Writing manifest to image destination
Storing signatures
STEP 2/6: COPY . /app
--> 884cc1b47a3
STEP 3/6: WORKDIR /app
--> 3e5773ea7e6
STEP 4/6: RUN pip install -r requirements.txt
....

STEP 5/6: EXPOSE 8080/tcp
--> 40420ac2e63
STEP 6/6: ENTRYPOINT ["python","run.py"]
COMMIT kube-lab:1.0
--> e64f30054cb
Successfully tagged localhost/kube-lab:1.0
e64f30054cbdd054c4a4c797f94b14683a3e04da91e6fc130340093814d51947
```

## List images available locally

``` bash
podman images

REPOSITORY                TAG         IMAGE ID      CREATED      SIZE
localhost/kube-lab        1.0         e64f30054cbd  6 hours ago  142 MB
docker.io/library/python  3.8-slim    acd4c2e29755  6 days ago   130 MB
```

As you can see, we have 2 images available, the base image we have downloaded as starting point for our application, and the actual image we have built.

## Execute images locally

To test that everything works just fine, we will execute the image locally always thanks to docker / podman.
We will have to map a port of our workstation to the port of the container which is exposing the service (remember the **EXPOSE** instruction in the Dockerfile): this operation is called **port-forwarding**.

``` bash
podman run -d -p <WORKSTATION_PORT>:<CONTAINER_PORT> <IMAGE_NAME>:<IMAGE_VERSION>
```

the `-d` option stands for detach, as in general we want to execute the docker in background, keeping the shell prompt to perform other tasks.

example:

``` bash
podman run -d -p 3000:8080 kube-lab:1.0
```

Check that everythin works by opening a browser window at `localhost:3000`

## Stop the container

to stop the container, list the processes and then issue the `stop` command with the proper `CONTAINER ID`

``` bash
podman ps -a

CONTAINER ID  IMAGE                   COMMAND     CREATED      STATUS          PORTS                   NAMES
d2f9431db2a7  localhost/kube-lab:1.0              6 hours ago  Up 6 hours ago  0.0.0.0:3000->8080/tcp  objective_knuth


podman stop d2f9431db2a7

d2f9431db2a7
```

## For future reference - delete container and images

To delete an image, you need to make sure that no container (even stopped ones) is using the image.
These are the steps

- list all containers and remove the ones using the selected image with

    `podman ps -a`

    `podman rm <CONTAINER ID>`

- list all images and remove selected image with

    `podman images`

    `podman rmi <IMAGE ID>`
