#!/usr/bin/node
const { argv } = require('node:process');

if (argv[1] === null) {
  console.log('No Argument');
} else {
  console.log('Argument found');
}
