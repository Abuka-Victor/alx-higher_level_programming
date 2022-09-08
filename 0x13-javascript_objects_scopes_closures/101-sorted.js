#!/usr/bin/node
const myDict = require('./101-data').dict;
const newDict = {};
for (let i in myDict){
  if (newDict.hasOwnProperty(myDict[i])) {
    newDict[myDict[i]].push(i);
  } else {
    newDict[myDict[i]] = [i];
  }
}
console.log(newDict);
