#!/bin/zsh

#for loop
for number in 1 2 3 4 5 6 7 8 9 10
do
  echo $number
  sleep 0.5
done

echo "This is outside of for loop"

# same thing
for number in {1..10}
do
  echo $number
  sleep 0.5
done

echo "This is outside of for 2nd loop"

# true example to compress .log files in a folder
for file in logfiles/*.log
do
  tar -czvf $file.tar.gz $file
done
echo "Going to logfiles directory"
cd logfiles; ls -lrt