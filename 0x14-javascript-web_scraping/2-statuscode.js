#!/usr/bin/node
const request = require('request');
request.get(process.argv[1]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
