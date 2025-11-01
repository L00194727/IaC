#!/bin/bash
# By: Edmund Connolly
# Date: 30 OCT 2025
# Function: Calculations
# Script: script15

echo "This script adds two numbers together"

# Check to see if we have two arguments
if [ $# -ne 2 ]
then
  echo "Usage - $0 x y"
  echo "Where x and y are summed"
  exit 1
else
  echo "$1 plus $2 is `expr $1 + $2`"
fi
 
exit 0
