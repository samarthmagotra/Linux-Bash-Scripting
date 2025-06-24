#!/bin/zsh

finished=0

while [ $finished -ne 1 ]
do
  echo "What is your fav Linux distribution?"

  echo "1 - Arch"
  echo "2 - CentOS"
  echo "3 - Debian"
  echo "4 - Mint"
  echo "5 - Ubuntu"
  echo "6 - Something else..."

  read distro;

  case $distro in
    1) echo "Arch is your choice";;
    2) echo "CentOS is your choice";;
    3) echo "Debian is your choice";;
    4) echo "Mint is your choice";;
    5) echo "Ubuntu is your choice";;
    6) echo "There are many distributions out there";;
    7) finished=1;;
    *) echo "You did not enter any choice"
  esac
done

echo "Thank you for using script!"
