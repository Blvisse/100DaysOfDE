#!/bin/bash

a=10;
b=20;
c=10;

# echo $(($a +$1))
echo $(($a + $b))
echo $(($a * $b + $c))

#using the expr command to carry out arithmetic operations

expr $a + $b 

echo '$a / $b'