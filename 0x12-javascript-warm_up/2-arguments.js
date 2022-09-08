#!/usr/bin/node
const { argv } = require('node:process');

if (argv[2] === undefined) {
  console.log('No argument');
} else if (argv[3] !== undefined) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
