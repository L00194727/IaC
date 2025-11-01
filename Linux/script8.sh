#!/bin/bash
# By: Edmund Connolly
# Date: 30OCT2025
# Function: While loop example
# Script: script8

INPUT_STRING=hello 
while [ "$INPUT_STRING" != "bye" ] 
do   
    echo "Please type something in (bye to quit)"   
    read INPUT_STRING   
    echo "You typed: $INPUT_STRING" 
done
exit 0
