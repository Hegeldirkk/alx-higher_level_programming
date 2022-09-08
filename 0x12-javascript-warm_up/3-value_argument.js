#!/usr/bin/node
const { argv } = require('node:process');

let value = '';
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  argv.forEach((val, index) => {
  if (index < 2) {
  value = '';
  } else {
  value = value + ' ' + val;
  }
  });
  console.log(value);
}
