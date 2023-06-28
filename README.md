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
A docker python file is executed using the python command followed by its inline arguments.
The files remain indifferent to each other, but each service is now in an encapsulated executable form (Docker image).
<br>
![Level 2](/resources/Docker-Level-2.png)
<br>


<hr>

Execution Instructions:

1. Open the project in IntelliJ.
2. cd into a specific level's directory.
3. Follow the instructions in the README.md file within the respective directory.

<hr>