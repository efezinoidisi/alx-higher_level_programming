#!/usr/bin/node
// displays the title of a Star wars movie based on an id

const request = require('request');
const url = process.argv[2];
// const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) console.log(error);
  const data = JSON.parse(body);
  const result = data.results[0].characters.filter(e => e.includes('18'))[0];
  request(result, (error, response, body) => {
    if (error) console.log(error);
    const films = JSON.parse(body).films;
    console.log(films.length);
  });
});
