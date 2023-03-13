#!/usr/bin/node

const size = process.argv.slice(2).length;
if (size === 0) {
  console.log('No argument');
} else if (size === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
