#!/usr/bin/node

const num = process.argv[2];

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < num; j++) {
    let i = 0;
    let s = '';
    while (i < num) {
      s += 'X';
      i++;
    }
    console.log(s);
  }
}
