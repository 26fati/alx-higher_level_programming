#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request(url, (err, res, body) => {
  body = JSON.parse(body);
  console.log(err || body.title);
});
