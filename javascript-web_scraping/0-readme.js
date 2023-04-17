#!/usr/bin/node

const fs = require('fs');

const filepath = process.argv[2];

fs.readfile(filepath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
