#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, req, body) => {
  body = JSON.parse(body);
  let count = 0;
  const results = body.results;
  results.forEach(element => {
    element.characters.forEach(ele => {
      if (ele.endsWith('/18/')) {
        count++;
      }
    });
  });
  console.log(err || count);
});
