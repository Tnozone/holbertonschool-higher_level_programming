#!/usr/bin/node

const first = process.argv[2];
const num = Number(first);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
