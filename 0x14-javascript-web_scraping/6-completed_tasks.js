#!/usr/bin/node
// computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  const todos = JSON.parse(body);
  const obj = {};
  for (const todo of todos) {
    if (todo.completed) {
      const key = todo.userId;
      if (obj[key]) {
        obj[key] += 1;
      } else {
        obj[key] = 1;
      }
    }
  }
  console.log(obj);
});
