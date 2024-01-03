#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, (err, req, body) => {
  if (err) {
    console.log(err);
  }
  body = JSON.parse(body);
  const result = body.results[id - 1];
  result.characters.forEach(element => {
    request(element, (err, requ, response) => {
      response = JSON.parse(response);
      console.log(err || response.name);
    });
  });
});
