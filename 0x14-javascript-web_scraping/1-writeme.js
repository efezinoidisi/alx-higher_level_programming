#!/usr/bin/node
// writes a string to a file
const fs = require('fs');
const [filename, content] = process.argv.slice(2);

try {
  fs.writeFileSync(filename, content, 'utf8');
} catch (err) {
  console.log(err);
}
