#!/bin/bash

greetings="Wagwan !"
user=$(whoami)
day=$(date +"%A")

echo "Welcome to our 100 Days of DE bash script"
echo "Today is $day and it is a great day to be $user"
echo "Your bash version is $BASH_VERSION"