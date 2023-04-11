#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  let res = 1;
  for (let i = 1; i <= n; i++) {
    res *= i;
  }
  return res;
}

const num = process.argv[2];
const res = factorial(num);
console.log(res);
