#!/bin/bash

#this script evaluates two numberic variables and returns the boolean result

a=1;b=2;c=3;d=4;

function compare_number {
    if [ $a -eq $b ]
    then
        echo "a is equal to b"
    else
        echo "a is not equal to b"
    fi

    if [ $b -ne $c ]
    then
        echo "$b is not equal to $c"
    else
        echo "$b is equal to $c"
    fi
    # then
    #     echo "$a is not equal to $b"
    # else
    #     echo "$a is equal to $b"
    

    if [ $c -lt $d ]
    then
    echo "c is less than d"
    else
    echo "c is not less than d"
    fi
}

compare_number 2> compare_number_warning.txt
