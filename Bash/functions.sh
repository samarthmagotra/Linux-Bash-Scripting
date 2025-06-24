#!/bin/zsh

#release_file=/etc/os-release
logfile=updater.log
errorlog=updater_errors.log
sw_vers >> version.log
release_file=version.log
echo $release_file

# function, which can be re-used
check_exit_status() {
  if [ $? -ne 0 ]
  then
    echo "An error occurred, please check $errorlog file "
  fi
}
# Or(||) statement with if, to check two conditions with same action. && can also be used
if grep -q "macOS" $release_file || grep -q "Ubuntu" $release_file
then
  brew update -y 1>>$logfile 2>>$errorlog
  check_exit_status
  #if [ $? -ne 0 ]
  #then
  #  echo "An error occurred, please check $errorlog file "
  #fi
fi
