#!/bin/bash
# Take in URL, POST key:vals
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
