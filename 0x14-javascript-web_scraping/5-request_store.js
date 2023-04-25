#!/usr/bin/node
// gets the content of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const [url, filename] = process.argv.slice(2);

request(url).pipe(fs.createWriteStream(filename));
