import hello;

hello.amogh("aram o")

# .pyc -> compiled python (frozen binary)
# works on pvc(python virtual machine)
# pvc is run time engine

# python code is coverted into byte code whiich is not a machine code
# then byte code goes to pvm

from importlib import reload

reload(hello)

print(hello.chai_one)