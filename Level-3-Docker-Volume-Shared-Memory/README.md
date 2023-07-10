<h2><b>Level 3</b></h2>
<h3>
Docker Volume shared Memory
</h3>
By <u>manisha-deshpande</u>
<hr>
Python version used: <b>3.11.3</b>
<hr>
<b>USAGE EXAMPLES on CMD (Command Prompt):</b>
<p>Make sure you are in the Level-3 directory</p>

<p>$ docker volume create db-volume</p>
<p>$ docker build -t plus -f Dockerfile.plus .</p>
<p>$ docker build -t minus -f Dockerfile.minus .</p>
<p>$ docker build -t multiply -f Dockerfile.multiply .</p>
<p>$ docker build -t divide -f Dockerfile.divide .</p>
<p></p>
<p>$ docker run --mount source=db-volume,target=/db plus 25</p>
25
<p>$ docker run --mount source=db-volume,target=/db plus 25</p>
50
<p>$ docker run --mount source=db-volume,target=/db minus 25</p>
-25
<p>$ docker run --mount source=db-volume,target=/db multiply 4</p>
40
<p>$ docker run --mount source=db-volume,target=/db divide 25</p>
4
<p></p>