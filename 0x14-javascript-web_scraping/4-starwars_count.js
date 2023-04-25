#!/usr/bin/node
// displays the number of movies where the character 'Wedge Antilles' is present

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  const data = JSON.parse(body);
  const result = data.results
    .filter(data => data.characters
      .find(character => character.includes('18')));
  console.log(result.length);
});
