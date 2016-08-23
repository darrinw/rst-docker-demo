.. _technical_delivery:

.. header::

    XYZ Configuration Management Solution Design

    Version 1.0

.. footer::

    Page ###Page### of ###Total###

Technical Delivery
==================

Overview
--------

The key components of the solution include:

  1. Rackspace Cloud Servers
  #. CHEF Automation
  #. Continuous Intgration Server
  #. GitHub



Who's Who
~~~~~~~~~

These are the parties that interact with the system.


* **Rackspace Professional Services** ("Rackspace PS"): Rackspace PS has designed and implemented
  the System described by this document.

* **Rackspace Support**: Rackspace Support refers to Rackspace services provided under the
  Intensive Support level and by the Network Security team ("NetSec").


Workflow Diagram
----------------

The diagram below is a high level out-line for the process flow of the Automation.

.. image:: https://www.lucidchart.com/publicSegments/view/ea74a757-b8fb-46ec-ba75-68bf1a0429fa/image.png
   :width: 100%

Automation Setup
----------------

Pre-Automation steps
~~~~~~~~~~~~~~~~~~~~




Assumptions
~~~~~~~~~~~

Some assumptions have been made as part of the automation.

  * Network Drives have the required packages and SSL certificates

Common Automation Tasks
-----------------------

Below is a description for common automation tasks.

Provision New Server
~~~~~~~~~-----~~~~~~

Change Server Role
~~~~~~~~~~~~~~~~~~

Remove a Server from CHEF
~~~~~~~~~~~~~~~~~~~~~~~~~

Check Server Automation Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add New OS Packages
~~~~~~~~~~~~~~~~~~~

Remove OS Packages
~~~~~~~~~~~~~~~~~~

Add 3rd Party Packages
~~~~~~~~~~~~~~~~~~~~~~

Remove 3rd Party Packages
~~~~~~~~~~~~~~~~~~~~~~~~~

Add a new User
~~~~~~~~~~~~~~

Remove a User
~~~~~~~~~~~~~

Modify a User
~~~~~~~~~~~~~


Rackspace Cloud Servers
-----------------------

Cloud Server Image
~~~~~~~~~~~~~~~~~~

This image will be based on a CentOS 7 base build.

The base image will only contain:

* Rackspace support tools
* Rackspace monitoring

Rackspace Cloud
----------------

Rackspace Cloud Portal
~~~~~~~~~~~~~~~~~~~~~~


Project source code and automation assets.

:: 
 
  * Configuration Management code: CHEF
  * GitHub URL:


Client Registration in CHEF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The registration of a Client server into CHEF is a manual step in the process.


The canonical documentation resources, including source code.

* Built using Sphinx with ReStructuredText
* GitHub URL:

CHEF Config Management
----------------------

Build initial Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~




Server Roles
~~~~~~~~~~~~


The Configuration has been broken down into three types based on  servers:

  * Base
  * WebServer
  * ApplicationServer


Base Server Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

This configuration is common across all Servers, all servers with a role set to "Base" will have this configuration applied.

Some of the common areas configured are:

  * Time Zone
  * Local hosts file
  * Disable IPv6

Web Server Configuration
~~~~~~~~~~~~~~~~~~~~~~~~

This configuration is common across all Web Servers, all servers with a role set to "WebServer" will have this configuration applied.

Application Server Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This configuration is common across all Application Servers, all servers with a role set to "ApplicationServer" will have this configuration applied.


*Content pending*


Technical HowTo
---------------

Manuall Setup for Registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following outlines all the steps to manually setup a server for registration.


Install CHEF Client
~~~~~~~~~~~~~~~~~~~




Server Roles
~~~~~~~~~~~~

