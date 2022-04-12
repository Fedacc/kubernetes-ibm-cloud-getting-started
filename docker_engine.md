---
layout: default
title: Docker Engine Installation
nav_order: 2
---
# Docker Engine Installation

First of all, you need to have a docker engine installed on your machine.
For education and demos it is possible to use docker, while if you are using it for a commercial solution (for example working on a project), you will have to have a proper license.

> 📖 Commercial use of Docker Desktop in larger enterprises (more than 250 employees OR more than $10 million USD in annual revenue) now requires a paid subscription. The grace period for those that will require a paid subscription ends on January 31, 2022.

Some alternatives inlcude for example [podman](https://podman.io/) (which I am currently using).
For the purposes of this activity, the two experiences are identical.

## Installing Docker

get docker at the following link according to your operating system.

[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker)

## Installing podman

You can find [detailed installation instructions](https://podman.io/getting-started/installation) here for different operating systems.

On **macOS** (tested on Monterey 12.2.1) I issued the following commands after facing some problems, it seemed that the game changer was to add a specific name to the podman machine.

``` bash
brew install podman
```

initialize virtual machine (this will download a base image, might require some time and some bandwidth)

``` bash
podman machine init myvm
```

to start the virtual machine running podman, use the following command

``` bash
podman machine start myvm
```
