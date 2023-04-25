#!/usr/bin/node
// displays all characters of a star wars movie

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) console.log(error);
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) throw error;
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
