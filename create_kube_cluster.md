# Create a managed kubernetes cluster on IBM Cloud

In order to create a kubernetes cluster on IBM Cloud you have to create an account.
The starting point is to register on [IBM Cloud](https://cloud.ibm.com/registration)

> ❗️ **If you are an IBM employee**: please do register to IBM Cloud with your work email address

> ❗️ **If you are a student of a university**: IBM has some specific programs for the universities, so it is highly likely that you can access the [Academic Initiative](https://https://www.ibm.com/academic/)! Reach out to your professors to learn more.

![IBM Cloud Registration form](/img/ibm-cloud-registration.png)

## Select the service from the catalog

![IBM Cloud landing page](/img/ibm-cloud-landing.png)

Once you are logged in to the portal, click on the **Catalog** link in the top banner (direct link [here](https://cloud.ibm.com/catalog))

Within the catalog, search for **Kubernetes Service** (or click the [following link](https://cloud.ibm.com/kubernetes/catalog/create))

In this page you will have the option to create a free cluster, which will be at your disposal for 30 days

> ❗️ after the 30 days expire, the cluster will be deleted (making it not suitable for production environment of course, also because the free cluster is a single node cluster with limited resources, thus leading to single point of failures to say the least.. so please for your real life scenarios consider using a **STANDARD** cluster)

In the cluster creation form, select the following parameters

| Param       | Value        |
| ----------- | ----------- |
| Pricing plan  | **Free**       |
| Cluster name   | **mycluster-free** or modify the name according to your preferences  |
| Cluster name   | **default** or select one *  |

> *: the resource group is a useful feature of **IBM Cloud** to logically segregate different projects within your account. You can also customize the visibility and access privileges of other users within the various resource group, making it ideal for projects in which RBAC is a thing (again, production environments are based on this!)

When all is set you will see a recap on the column on the right alongside with the option to actually CREATE the cluster.

![IBM Cloud create cluster](/img/ibm-cloud-kube-create.png)

Click on **CREATE**

> **Note**: this might require some time, as the cluster will be provisioned in your account with the setup of master node and worker node. You will be redirected to a page with a status of the operations on your cluster.

![IBM Cloud cluster status](/img/ibm-cloud-kube-status.png)