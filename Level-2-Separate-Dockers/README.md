<h2><b>Level 2</b></h2>
<h3>
Separate Dockers
</h3>
By <u>manisha-deshpande</u>
<hr>
Python version used: <b>3.11.3</b>
<hr>
<b>USAGE EXAMPLES on CMD (Command Prompt):</b>
<p>Make sure you are in the Level-2 directory</p>

<p>$ docker build -t plus -f Dockerfile.plus .</p>
<p>$ docker build -t minus -f Dockerfile.minus .</p>
<p>$ docker build -t multiply -f Dockerfile.multiply .</p>
<p>$ docker build -t divide -f Dockerfile.divide .</p>
<p></p>
<p>$ docker run plus 2 3</p>
5
<p></p>
<p>$ docker run minus 2 3</p>
-1
<p></p>
<p>$ docker run multiply 2 3</p>
6
<p></p>
<p>$ docker run divide 8 3</p>
2
<p></p>
<p>$ docker run plus 2 3 | docker run -i minus 4</p>
1
<p></p>