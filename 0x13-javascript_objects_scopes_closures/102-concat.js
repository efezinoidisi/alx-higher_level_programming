#!/usr/bin/node

// This script concatenates two files

const filePaths = process.argv.slice(2);
const fs = require('fs');
if (filePaths.length === 3) {
  const fd = fs.createWriteStream(filePaths[2]);
  const file1 = fs.readFileSync(filePaths[0]);
  const file2 = fs.readFileSync(filePaths[1]);
  fd.write(file1);
  fd.write('\n');
  fd.write(file2);
  fd.write('\n');
  fd.end();
}
