#!/bin/zsh

#While loops
myvar=1
while [ $myvar -le 10 ] #le - less than or equal to 10
do
  echo $myvar
  myvar=$(( $myvar +1 ))
  sleep 0.5
done

myvar=1
while [ -f ~/testfile ]
do
  echo "As of $(date), Test file exists"
  sleep 5
done
echo "As of $(date), File no longer exists"