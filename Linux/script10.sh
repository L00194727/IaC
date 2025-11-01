#!/bin/bash
# By: Edmund Connolly
# Date: 30 Nov 2025
# Function: Simple number check
# Script: script10

read -p "Enter value for X: " X
# Check if less than
if [ "$X" -lt "0" ]
then
    echo "X is less than zero"
    exit 0
else
    echo "X is greater than zero"
    exit 0
fi
