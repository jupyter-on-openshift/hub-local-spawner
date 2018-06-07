JupyterHub (Local Spawner)
--------------------------

This repository contains an example of a customised deployment of JupyterHub for OpenShift, which creates notebook instances as local processes within the same pod as JupyterHub is running. It uses an image for running JupyterHub on OpenShift as an S2I builder to create the customised image containing configuration to use the local process spawner. Along with JupyterHub, a PostgreSQL database is run. These run in separate containers of a single pod. A persistent volume is used to store data for both the database and JupyterHub. Any work done through a Jupyter notebook instance is also persistent across restarts.

Loading the Templates
---------------------

A template is provided for deploying this example. The one template will create a build configuration for creating the base image for JupyterHub. This image is S2I enabled, and a second build configuration is then used to create the customised JupyterHub with configuration from this repository. A deployment configuration, service and route is also created, to deploy the JupyterHub instance and make it available.

To load the template run:

```
oc create -f https://raw.githubusercontent.com/jupyter-on-openshift/poc-hub-local-spawner-1/master/templates.json
```

This will create the following templates:

```
poc-hub-local-spawner-1
```

Deploying the Example
---------------------

The create the images and deploy the example, run:

```
oc new-app --template poc-hub-local-spawner-1
```

The name of the deployment created will be ``poc-hub-local-spawner-1``. If you want to change the name, instead run:

```
oc new-app --template poc-hub-local-spawner-1 \
  --param APPLICATION_NAME=jupyterhub
```

Once JupyterHub has finished deploying open it from your browser.

With the template loaded, you could also instead have deployed the example by selecting _Add to Project_, then _Select from Project_, in the web console and selecting on _JupyterHub Local Spawner POC#1_ from the available templates.

To see a description of the template, what resources it creates and the parameters it accepts, run:

```
oc describe template/poc-hub-local-spawner-1
```

Deleting the Application
------------------------

To delete the example JupyterHub instance which was deployed, run:

```
oc delete all,configmap,pvc --selector app=poc-hub-local-spawner-1
```
