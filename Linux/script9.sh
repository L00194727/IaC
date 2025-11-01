#!/bin/bash
# By: Edmund Connolly
# Date: 30 OCT 2025
# Function: Check language for hello greeting
# Script: script9

echo "press [ctrl][c] to exit"

while read f
do
case $f in
    Hello)              echo English ;;
    "Dia Duit")         echo Irish ;;
    Ciao)               echo Italian ;;
    *)                  echo Unknown: $f
;;
esac
done
exit 0
