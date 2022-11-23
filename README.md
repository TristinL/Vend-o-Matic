Vend-O-Matic.

Project languages: Python, Docker

Project Description:
Python server utilizing Flask. This project demonstrates my ability to create a server,
implement HTTP methods, develop unittests, and dockerize the entire project.

It replicates a system for a vending machine. At least two coins must be inserted into the
machine in order to dispense a product. More than two coins can be inserted but only one
product will be dispensed per transaction. Excess coins will be returned at the end of the
transaction.

In order to reduce dependencies, there is no database holding the products. Instead we use
a simple vending.json file to store the quantities and IDs of products.

File overview:
* flaskAPI.py - main program
* reset_vending.py - used to reset the vending machine's inventory file (vending.json)
* test_api.py - unittest for project
* vending.json - inventory file for the project
* requirements.txt - requirements of the project used by Dockerfile
* Dockerfile - docker instructions
* docker-compose.yml - compose file for docker to create the project

Installation instructions:
* Download the Zip
* Extract it on your machine
* Open terminal
* cd into the directory "Vend-o-Matic-main"
* Open Docker on your machine if it is not already running
* In terminal type "docker-compose up"
* The image should build and the container should startup.
* Once done, open Postman on your machine, or any program capable of sending GET, PUT, and DELETE calls.
* You can now send GET, PUT, and DELETE calls to the server on http://0.0.0.0:5001