#!/bin/zsh

# arguments: $1 - first argument, $2, $3...
#echo "You entered the argument: $1, $2, $3"
#ls -lh $1

echo "Script to check number of objects in any directory. Example Usage -- sh arguments.sh /usr"
lines=$(ls -lh $1 | wc -l)
if [ $# -ne 1 ]   #--  $# takes the argument provided by user with script at command line, like 1,2 ..
then
  echo "Script require exactly one directory path passed to it"
  exit 1
fi
echo "You have $(($lines-1)) objects in the $1 directory."