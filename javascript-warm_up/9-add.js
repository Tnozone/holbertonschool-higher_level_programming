#!/usr/bin/node

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
let result = 0;
result = add(process.argv[2], process.argv[3]);
console.log(result);
