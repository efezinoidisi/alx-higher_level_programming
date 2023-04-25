#!/usr/bin/node
// displays the status code of a GET request

const request = require('request');
const url = process.argv[2];

request.get(url).on('response', (res) => {
  console.log(`code: ${res.statusCode}`);
});
