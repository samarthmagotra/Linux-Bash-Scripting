#!/bin/zsh

#release_file=/etc/os-release
sw_vers >> version.log
release_file=version.log
echo $release_file
# Or(||) statement with if, to check two conditions with same action. && can also be used
if grep -q "macOS" $release_file || grep -q "Ubuntu" $release_file
then
  brew update
fi

#IMPORTANT NOTES

#To make a script universally available, instead of just at your local directory,
# put script in /usr/local/bin/, which is in $PATH

#(base) samarthmagotra@Samarth-MacBook-Air Bash % echo $PATH
#/Users/samarthmagotra/anaconda3/bin:/Users/samarthmagotra/anaconda3/condabin:/Library/Frameworks/Python.framework/Versions/3.13/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/Library/Frameworks/Python.framework/Versions/3.9/bin:
# /usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Applications/Wireshark.app/Contents/MacOS

#sudo mv universal_update_script.sh /usr/local/bin/universal_update_script
#ls -l /usr/local/bin/universal_update_script
#sudo chown root:root /usr/local/bin/universal_update_script
#sh universal_update_script    ---  No .sh extension needed to run in Linux
