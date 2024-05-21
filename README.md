<h1>Python</h1> <br>
 .pyc -> compiled python (frozen binary) <br>
 works on pvc(python virtual machine)<br>
 pvc is run time engine<br>
 python code is coverted into byte code whiich is not a machine code<br>
 then byte code goes to pvm
 <h2>Immutable and mutable</h2>
immutable-who value cannot be changed <br>
 Numbers (int, float, complex) <br>
Once a number is assigned to a variable, it cannot be changed. For example: <br>
 x = 5 <br>
x = x + 1  # A new object is created with the value 6 <br>
 Strings <br>
Strings are immutable in Python. If you try to modify a string, a new string object will be created instead. For example: <br>
s = "Hello" <br>
 s = s + " World"  # A new string object is created with the value "Hello World"p <br>
Tuples <br>
 Tuples are ordered collections of elements and are immutable. Once a tuple is created, you cannot modify its elements. For example: <br>
 t = (1, 2, 3) <br>
t[0] = 4  # This will raise a TypeError since tuples are immutable <br>
 <br>
 <b>mutable</b>: list,dictionaries, array , set<br>
