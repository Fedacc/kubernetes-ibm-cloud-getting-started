---
layout: default
title: Push image to Registry
nav_order: 6
---

# Push image to Registry

The goal of this step is to push the locally build image to the container registry [documentation](https://cloud.ibm.com/docs/containers?topic=containers-registry).
We are going to publish the image in the [IBM Cloud Container Registry](https://cloud.ibm.com/docs/Registry?topic=Registry-getting-started#getting-started).

## Install the IBM Cloud CLI

Install the IBM Cloud CLI so that you can run the IBM Cloud `ibmcloud` commands

For MacOS, run the following command:

``` bash
curl -fsSL https://clis.cloud.ibm.com/install/osx | sh
```

For Linux™, run the following command:

``` bash
curl -fsSL https://clis.cloud.ibm.com/install/linux | sh
```

For Windows™ 10 Pro, run the following command in PowerShell as an administrator:

``` bash
iex(New-Object Net.WebClient).DownloadString('https://clis.cloud.ibm.com/install/powershell')
```

For WSL2 on Windows™, run the following command:

``` bash
curl -fsSL https://clis.cloud.ibm.com/install/linux | sh
```

### Verify the IBM Cloud CLI installation

``` bash
ibmcloud help

ibmcloud help
NAME:
  ibmcloud - A command line tool to interact with IBM Cloud
  Find more information at: https://ibm.biz/cli-docs

USAGE:
  [environment variables] ibmcloud [global options] command [arguments...] [command options]

VERSION:

....
```

## Installing IBM Cloud Container Registry CLI plug-in

``` bash
ibmcloud plugin install container-registry
```

## Create a namespace in the container registry

The following guide creates a namespace on the container registry via a terminal.
Optionally, you can perform the same activity on the [Container Registry dashboard](https://cloud.ibm.com/registry/start)

- Log in to your IBM Cloud account

    ``` bash
    ibmcloud login -a https://cloud.ibm.com
    ```

    > ❗️ If you are using a federated ID (such as via IBM), you need to add the `--sso`

    target the resource group of your cluster

    ``` bash
    ibmcloud target -g <RESOURCE GROUP>
    ```

- Ensure that you're targeting the correct IBM Cloud Container Registry region

    ``` bash
    ibmcloud cr region-set eu-de
    ```

- Choose a name for your namespace, and create that namespace. Use this namespace for the rest of the lab

    ``` bash
    ibmcloud cr namespace-add lab-kube
    ```

- Log your local container engine daemon into the IBM Cloud Container Registry

    Using docker:

    ``` bash
    ibmcloud cr login --client docker
    ```

    Using podman:

    ``` bash
    ibmcloud cr login --client podman
    ```

- Choose a repository and tag by which you can identify the image. Use the same repository and tag for the rest of thie lab

    Using docker:

    ``` bash
    docker tag kube-lab:1.0 de.icr.io/lab-kube/kube-lab:1.0
    ```

    using podman:

    ``` bash
    podman tag kube-lab:1.0 de.icr.io/lab-kube/kube-lab:1.0
    ```

- Push the image

    Using docker:

    ``` bash
    docker push de.icr.io/lab-kube/kube-lab:1.0
    ```

    using podman:

    ``` bash
    podman push de.icr.io/lab-kube/kube-lab:1.0
    ```

- Verify that the image was pushed

    ``` bash
    ibmcloud cr image-list
    ```
