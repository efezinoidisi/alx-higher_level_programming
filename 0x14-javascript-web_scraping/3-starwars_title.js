#!/usr/bin/node
// displays the title of a Star wars movie based on an id

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) throw error;
  const data = JSON.parse(body);
  console.log(data.title);
});
