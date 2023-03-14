#!/usr/bin/node

const args = process.argv.slice(2);
const sArgs = args.map(arg => parseInt(arg));
sArgs.sort((a, b) => a - b);

if (sArgs.length === 0 || sArgs.length === 1) {
  console.log(0);
} else {
  console.log(sArgs[sArgs.length - 2]);
}
