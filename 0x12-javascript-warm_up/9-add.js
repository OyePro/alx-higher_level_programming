#!/usr/bin/node

const args = process.argv;
const a = +args[2];
const b = +args[3];
function add (a, b) {
  return (a + b);
}
console.log(add(a, b));
