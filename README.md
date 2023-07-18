# Calculator-services-Docker

Author: Manisha Malhar Rao Deshpande

This is a python-docker project.
 
<hr>
About:

Creating 4 python services (plus, minus, multiply, divide)
and building them at 4 levels, one more complex than the previous.
<br>
<br>
<b>Level 1: Python Command</b>
<br>
Each python file is executed using the python command followed by its inline arguments.
This is the simplest level as the files are indifferent to each other.
<br>
![Level 1](/resources/Docker-Level-1.png)
<br>

<b>Level 2: Separate Dockers</b>
<br>
Each python file is executed within its respective docker container. Images are built and executed using the docker build and docker run commands respectively.
The services remain indifferent to each other, but each one is now in an encapsulated executable form (Docker image).
<br>
![Level 2](/resources/Docker-Level-2.png)
<br>

<b>Level 3: Docker Volume</b>
<br>
Each python file is executed within its respective docker container. However, a docker volume is created which is used to persist data and can be mounted onto other containers.
In this level, a docker volume is created using the <i>docker volume create</i> command and the Dockerfiles create a directory called "db". The <i>docker run</i> command mounts a volume named "db-volume" to the "/db" directory in the container.
<br>
Every run can now access previously stored data and manipulate it. In this project, each service accesses it's previously stored result, starting with the default value of 0(for plus, minus), 10(for multiply), 100(for divide), and performs arithmetic operations on it and stores the updated result in it's respective file within "/db".
<br>
![Level 3](/resources/Docker-Level-3.png)
<br>

<b>Level 4: Docker Compose with UI</b>
<br>
A docker compose file is created to run all the services at once. Furthermore, a docker volume is created which enables data sharing between multiple running containers.
The services are now capable of manipulating and using data in the shared memory.
<br>
<!--![Level 4](/resources/Docker-Level-4.png)-->
<br>

<hr>

Execution Instructions:

1. Open the project in IntelliJ.
2. cd into a specific level's directory.
3. Follow the instructions in the README.md file within the respective directory.

<hr>