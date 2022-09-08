#!/usr/bin/node
if (process.argv.length === 2 || !Number.parseInt(process.argv[2])) {
  console.log('Missing size');
} else if (process.argv[2] > 0) {
  let value;
  for (let i = 0; i < process.argv[2]; i++) {
    value = '';
    for (let j = 0; j < process.argv[2]; j++) {
      value = value + 'X';
    }
    console.log(value);
  }
}
