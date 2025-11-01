#!/bin/bash
# By: Edmund Connolly
# Date: 30 OCT 2025
# Function: Test for File and Directory
# Script: script17

echo "This script checks a file and directory to see if they exist"

# Check to see if we have two arguments
if [ $# -ne 2 ]
then
  echo "Usage - $0 x y"
  echo "Where x and y are FileName and Directory"
  exit 1
fi

if [ -f $2/$1 ]
then
  echo "This filename [$1] exists"
elif [ -d $1 ]
then
  echo "This dirname [$2] exists"
else
  echo "Neither [$2] or [$1] exist"
fi
 
exit 0
