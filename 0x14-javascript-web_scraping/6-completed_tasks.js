#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, req, body) => {
  body = JSON.parse(body);
  const dic = {};
  let i = 1;
  body.forEach(element => {
    let count = 0;
    while (element.userId === i) {
      if (element.completed === true) {
        count++;
      }
    }
    dic[i] = count;
    i++;
  });
  console.log(err || dic);
});
