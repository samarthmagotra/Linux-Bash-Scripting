#!/bin/zsh

#Exit codes for errors -- variable '?', 0 is no error, 1 or any other non zero exit code is an error
ls -l /root
echo $?

package=noexit
brew install $package
echo "The exit code for the package installed is: $?"

#package=htop
package=noexit
brew install $package
if [ $? -eq 0 ]
then
  echo "The installation of $package is success"
  echo "New command is availabe here:"
  which $package
else
  echo "$package failed to installed"
fi

#append output in file
#package=htop
package=noexit
brew install $package >> package_install_result.log
if [ $? -eq 0 ]
then
  echo "The installation of $package is success"
  echo "New command is availabe here:"
  which $package
else
  echo "$package failed to installed" >> package_failure_result.log
fi

# using directory, every command has an exit code
directory=/noexit
if [ -d $directory ]
then
  echo "The 1st exit code is: $?"
  echo "The directory $directory exists.."
  echo "The 2nd exit code is: $?"
else
  echo "The 1st exit code is: $?"
  echo "The directory $directory does not exists..."
  echo "The 2nd exit code is: $?"
fi

echo "Hello world"
#exit 1 # Exit the script with whatever exit code you write, next line will never execute
echo $?

directory=/etc
if [ -d $directory ]
then
  echo "The directory $directory exists.."
  exit 0
else
  echo "The directory $directory does not exists..."
  exit 1
fi

#These lines will never execute becasue of exit above, it will exit from script
echo "Hi"
echo "How are you"