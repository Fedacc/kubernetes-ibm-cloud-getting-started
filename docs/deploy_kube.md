---
layout: default
title: Deploy to Kubernetes
nav_order: 7
---

# Deploy to Kubernetes

The goal of this step is to create a pod in the Kubernetes cluster running the image we have pushed to the container registry

## Installing IBM Cloud Kubernetes Service CLI plug-in

To create and manage Kubernetes clusters in IBM Cloud® Kubernetes Service.
To install the Kubernetes Service plug-in, run the following command:

``` bash
ibmcloud plugin install container-service
```

## Download the Kubernetes CLI

Sometimes it is just better to execute directly the kubernetes commands without passing through the Kubernetes Service CLI.
Download the proper CLI according to your operating system

- [OS X](https://storage.googleapis.com/kubernetes-release/release/v1.10.8/bin/darwin/amd64/kubectl)
- [Linux](https://storage.googleapis.com/kubernetes-release/release/v1.10.8/bin/linux/amd64/kubectl)
- [Windows](https://storage.googleapis.com/kubernetes-release/release/v1.10.8/bin/windows/amd64/kubectl.exe)

Install for macOS and Linux:

1. Move the executable file to the `/usr/local/bin` directory using the command `mv /<path_to_file>/kubectl /usr/local/bin/kubectl`

2. Make sure that `/usr/local/bin` is listed in your PATH system variable.

    ``` bash
    $ echo $PATH
    /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
    ```

3. Convert the binary file to an executable: `chmod +x /usr/local/bin/kubectl`

Install for Windows:
Install the Kubernetes CLI in the same directory as the IBM Cloud CLI. This setup saves you some filepath changes when you run commands later.

## Update the configuration files

In the project you can find under the folder `/kubernetes` you can find a simple `yaml` file that describes a deployment in Kubernetes: it is composed by a deployment (to create the pod) and a service.

Rename the `template.deployment.yaml` to `deployment.yaml` and change its content with the proper values such as the **container registry image info**.

## Log in to the cluster

Make sure that you are already logged in with IBM Cloud

``` bash
ibmcloud login -a https://cloud.ibm.com
```

> ❗️ If you are using a federated ID (such as via IBM), you need to add the `--sso`

target the resource group of your cluster

``` bash
ibmcloud target -g <RESOURCE GROUP>
```

- List the clusters in your account:

    ``` bash
    ibmcloud ks clusters
    ```

- Set an environment variable that will be used in subsequent commands in this lab

    ``` bash
    export CLUSTER_NAME=<your_cluster_name>
    ```

- Configure `kubectl` to point to your cluster

    ``` bash
    ibmcloud ks cluster config --cluster $CLUSTER_NAME
    ```

- Validate proper configuration

    ``` bash
    kubectl get namespace

    NAME              STATUS   AGE
    default           Active   125m
    ibm-cert-store    Active   121m
    ibm-system        Active   124m
    kube-node-lease   Active   125m
    kube-public       Active   125m
    kube-system       Active   125m
    ```

> 💡 For this lab, we will use the `default` namespace. If you wish to deploy things to different namespaces on the cluster, remember that you need to add the `-n <NAMESPACE NAME>` at the end of your commands

## Create config map

You can use `kubectl create configmap` with the `--from-literal` argument to define a literal value from the command line

``` bash
kubectl create configmap python-simple-app-config --from-literal=PYTHON_CUSTOM_MESSAGE="Hello from the cloud"
```

## Apply the configuration

``` bash
kubectl apply -f kubernetes/deployment.yaml
```

## Check everything is working as expected

Check pods are in `Running` state

``` bash
kubectl get pods
```

Check service exists

``` bash
kubectl get services

kubectl get services
NAME                TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
kubernetes          ClusterIP   172.21.0.1      <none>        443/TCP          10h
python-simple-app   NodePort    172.21.73.100   <none>        8080:32459/TCP   7s
```

## Connect to the application

The free cluster unfortunately does not come with an Application Load Balancer (ALB), so we do not have an Ingress component that we can use to obtain an hostname to connect to.
As a workaround, we will directly contact the PUBLIC IP of the worker node and we will use the port exposed

1. To find the port used on the worker node, examine your new service

    ``` bash
    kubectl get services

    NAME                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
    kubernetes          ClusterIP   172.21.0.1       <none>        443/TCP          10h
    python-simple-app   NodePort    172.21.151.240   <none>        8080:32189/TCP   2m48s
    ```

    in my scenario the port is the **32189** for the service `python-simple-app`

2. obtain the EXTERNAL IP of your worker node

    ``` bash
    kubectl get nodes -o wide

    NAME             STATUS   ROLES    AGE   VERSION       INTERNAL-IP      EXTERNAL-IP       OS-IMAGE             KERNEL-VERSION       CONTAINER-RUNTIME
    10.144.214.101   Ready    <none>   10h   v1.22.8+IKS   10.144.214.101   159.122.177.130   Ubuntu 18.04.6 LTS   4.15.0-175-generic   containerd://1.5.11
    ```

    in my scenario the IP is **159.122.177.130**

3. Open a browser window at `http://<EXTERNAL_IP>:<PORT>` and everything *should* be working!
