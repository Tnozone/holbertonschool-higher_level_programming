#!/usr/bin/node

const args = process.argv.slice(2);
const tab = [];

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  for (const arg of args) {
    tab.push(Number(arg));
  }
  tab.sort((a, b) => b - a);
  console.log(tab[1]);
}
