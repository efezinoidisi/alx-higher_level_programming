#!/usr/bin/node
// displays all characters of a star wars movie

const request = require('request-promise');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

(async function () {
  try {
    const body = await request(url);
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const result = await request(character);
      const name = JSON.parse(result).name;
      console.log(name);
    }
  } catch (err) {
    console.log(err);
  }
})();
