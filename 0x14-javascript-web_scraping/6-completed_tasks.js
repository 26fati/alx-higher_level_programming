#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, req, body) => {
  body = JSON.parse(body);
  const dic = {};
  body.forEach(element => {
    if (element.completed === true) {
      if (dic[element.userId] === undefined) {
        dic[element.userId] = 1;
      } else {
        dic[element.userId] += 1;
      }
    }
  });
  console.log(err || dic);
});
