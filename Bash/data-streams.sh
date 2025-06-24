#!/bin/zsh

## STANDARD OUTPUT ##
#find type file
# find /etc -type f

#find and re-direct an error from output to /dev/null folder
# 1- standard output, 2- standard error
# find /etc -type f 2> /dev/null
# find /etc -type f 1> /dev/null OR # find /etc -type f > /dev/null

# send both standard output and standard error to a file
# find /etc -type f &> /dev/null

#send to two different files
#find /etc -type f 1> file1.txt 2> file2.txt

# >> for append and > for overwrite
#sudo apt update 1>>file1.txt 2>>file2.txt
#sudo apt update -y 1>>file1.txt 2>>file2.txt      --- -y option for 'yes' permission

#sudo find /etc -type f -print

## STANDARD INPUT ##
echo "Please enter your name:"
read Samarth
echo "Your name is: $Samarth"

