#!/usr/bin/node

const fs = require('fs');

const filepath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filepath, string, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
