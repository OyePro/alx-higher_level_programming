#!/bin/bash
# Take in URL, add header variable, displays "Hello Holberton School!"
curl -s -H "X-School-User-Id":98 "$1"
