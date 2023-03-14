#!/usr/bin/node

// This script imports an dictionary and computes a new dictionary of user ids by occurrences

const dict = require('./main.js').dict;
const newDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (newDict[value] === undefined) {
    newDict[value] = [];
  }
  newDict[value].push(key);
}
console.log(newDict);
