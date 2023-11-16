#!/usr/bin/node

const args = process.argv;
function secondBig (arr) {
  let first = -1;
  let second = -1;
  for (let i = 0; i < arr.length; i++) {
    if (+arr[i] > first) {
      second = first;
      first = +arr[i];
    } else if (+arr[i] > second && +arr[i] !== first) {
      second = +arr[i];
    }
  }
  return (second);
}
const arrays = [];
if (args.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    arrays.push(args[i]);
  }
  console.log(secondBig(arrays));
}
