JupyterHub (Local Spawner)
--------------------------

This repository contains an example of a customised deployment of JupyterHub for OpenShift, which creates notebook instances as local processes within the same pod as JupyterHub is running. It uses an image for running JupyterHub on OpenShift as an S2I builder to create the customised image containing configuration to use the local process spawner.

Loading the Templates
---------------------

A template is provide for deploying this example. The one template will create a build configuration for creating the base image for JupyterHub. This image is S2I enabled, and a second build configuration is then used to create the customised JupyterHub with configuration from this repository. A deployment configuration, service and route is also created, to deploy the JupyterHub instance and make it available.

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

Deleting the Application
------------------------

To delete the example JupyterHub instance which was deployed, run:

```
oc delete all,configmap,pvc --selector app=poc-hub-local-spawner-1
```

How does this Example Work
--------------------------

The repository for this example contains two main files which are consumed by the S2I build process for the customised JupyterHub image.

* [requirements.txt](requirements.txt) - This specifies that the ``notebook`` package should be installed as it would not normally be installed with JupyterHub.
* [.jupyter/jupyterhub_config.py](.jupyter/jupyterhub_config.py) - This sets as the spawner class a derived variant of the ``LocalProcessSpawner``. A derived variant is needed because it is necessary to ensure certain additional environment variables are passed to the Jupyter notebook process from JupyterHub. This is needed so that the Python runtime is found correctly, and that password file lookups for the user succeed. The custom variant of the spawner is also used to create a separate work directory for each user given a notebook instance.
