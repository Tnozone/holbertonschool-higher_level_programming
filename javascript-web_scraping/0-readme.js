#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

fs.readfile(filepath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});