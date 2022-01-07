#!/bin/bash

function user_details {

    user=$(whoami)
    date=$(date +"%A")
    echo "Welcome to our 100 Days of DE bash script"
    echo "Your details are as follows username: $user"
    echo "logged in on $date"

}

function total_files {

    
        echo "Total number of files in the current directory is $(ls -1 | wc -l)"
    
}

# function parameters{
#     param=$1
#     echo "The script was called with $param parameters"
# }

user_details 2> function_warning.txt
total_files 2> function_warning.txt

