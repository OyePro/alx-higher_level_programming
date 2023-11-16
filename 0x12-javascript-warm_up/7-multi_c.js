#!/usr/bin/node

const args = process.argv;
if (args.length <= 2 || isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < +args[2]; i++) {
    console.log('C is fun');
  }
}
