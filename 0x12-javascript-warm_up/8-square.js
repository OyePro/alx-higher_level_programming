#!/usr/bin/node

const args = process.argv;
if (args.length <= 2) {
  console.log('Missing size');
} else if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  const out = [];
  for (let i = 0; i < +args[2]; i++) {
    out.push('X');
  }
  for (let i = 0; i < +args[2]; i++) {
    console.log(out.join(''));
  }
}
