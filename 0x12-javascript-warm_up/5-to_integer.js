#!/usr/bin/node

const args = process.argv;
if (args.length <= 2) {
  console.log('Not a number');
} else if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + ~~args[2]);
}
