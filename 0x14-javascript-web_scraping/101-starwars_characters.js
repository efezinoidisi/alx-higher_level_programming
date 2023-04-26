#!/usr/bin/node
// displays all characters of a star wars movie

const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request)
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

(async function () {
  try {
    const body = await requestPromise(url);
    const characters = JSON.parse(body.body).characters;
    for (const character of characters) {
      const result = await requestPromise(character);
      const name = JSON.parse(result.body).name;
      console.log(name);
    }
  } catch (err) {
    console.log(err);
  }
})();
