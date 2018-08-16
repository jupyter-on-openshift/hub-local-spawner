JupyterHub (Local Spawner)
--------------------------

This repository contains an example of a customised deployment of JupyterHub for OpenShift, which creates notebook instances as local processes within the same pod as JupyterHub is running. It uses an image for running JupyterHub on OpenShift as an S2I builder to create the customised image containing configuration to use the local process spawner. Along with JupyterHub, a PostgreSQL database is run. These run in separate containers of a single pod. A persistent volume is used to store data for both the database and JupyterHub. Any work done through a Jupyter notebook instance is also persistent across restarts.


Deploying the Example
---------------------

A template is provided for deploying this example. The one template will create a build configuration for creating the base image for JupyterHub. This image is S2I enabled, and a second build configuration is then used to create the customised JupyterHub with configuration from this repository. A deployment configuration, service and route is also created, to deploy the JupyterHub instance and make it available.

To create a deployment directly from the template run:

```
oc new-app https://raw.githubusercontent.com/jupyter-on-openshift/poc-hub-local-spawner/master/templates.json
```

The name of the deployment created will be ``jupyterhub``. If you want to change the name, supply the additional option ``--param APPLICATION_NAME=jupyterhub``.

Once JupyterHub has finished deploying open it from your browser.

As a template is provided, you could also load the template into the project. This would then be selectable from the service catalog, or you could deploy from the loaded template on the command line.

Deleting the Application
------------------------

To delete the example JupyterHub instance which was deployed, run:

```
oc delete all,configmap,pvc --selector app=jupyterhub
```
