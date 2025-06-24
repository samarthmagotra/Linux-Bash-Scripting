#!/bin/zsh

#variables
FIRST_NAME="Samarth"
LAST_NAME="Magotra"
echo Hello $FIRST_NAME $LAST_NAME
echo "Hello, my first name is $FIRST_NAME and my last name is $LAST_NAME"
# This works only with "", not ''
echo 'Hello, my first name is $FIRST_NAME and my last name is $LAST_NAME'

#sub-shell
files=$(ls)
path=$(pwd)
echo "$files
$path"

#date
now=$(date)
echo "System time and date is"
echo $now

#default variable
echo "Your username is: $USER"
environment_variables=$(env)
echo "All default variables"
echo $environment_variables