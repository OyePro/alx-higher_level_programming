#!/usr/bin/node

const args = process.argv;
if (args.length >= 4) {
  console.log(args[2] + ' is ' + args[3]);
} else if (args.length === 3) {
  console.log(args[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
