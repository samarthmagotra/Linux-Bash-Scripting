#!/bin/zsh

#equal -eq
mynum=300
if [ $mynum -eq 200 ]
then
  echo "The condition is true."
else
  echo "The variable not equal 300"
fi

# !
mynum=300
if [ ! $mynum -eq 200 ]
then
  echo "The condition is true."
else
  echo "The variable not equal 300"
fi

#not equal - ne
mynum=300
if [ $mynum -ne 200 ]
then
  echo "The condition is true."
else
  echo "The variable not equal 300"
fi

#greater than - gt
mynum=300
if [ $mynum -gt 200 ]
then
  echo "The condition is true."
else
  echo "The variable not equal 300"
fi

#check if file or directory exists, -f for files and -d for directory
if [ -f ~/myfile ]
then
  echo "Files exists"
else
  echo "Files does not exists"
fi

#installing htop and running it
command=/opt/homebrew/bin/htop
if [ -f $command ]
then
  echo "$command is available, lets run it..."
  htop
else
  echo "$command is NOT availabe, installing it..."
  #sudo apt-get update && sudo apt-get install -y htop
  brew install htop
fi
#$command

#Another way
command=htop
if command -v $command
then
  echo "$command is available, lets run it..."
else
  echo "$command is NOT availabe, installing it..."
  #sudo apt-get update && sudo apt-get install -y htop
  brew install htop
fi
$command