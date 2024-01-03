#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, req, body) => {
  body = JSON.parse(body);
  let count = 0;
  const results = body.results;
  results.forEach(element => {
    if (element.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });
  console.log(err || count);
});
