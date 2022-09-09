#!/usr/bin/node
function add (a, b) {
  const add = a + b;
  console.log(add);
}

if (process.argv.length === 2 || process.argv[3] === undefined) {
  console.log('NaN');
} else {
  add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]));
}
