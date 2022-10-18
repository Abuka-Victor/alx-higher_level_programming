#!/usr/bin/node
const fs = require('fs');
const myargs = process.argv.slice(2);

fs.readFile(myargs[0], 'utf-8', (data, err) => {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
