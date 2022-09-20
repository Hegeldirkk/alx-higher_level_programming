#!/usr/bin/node
function factorial (x) {
  let res = 1;
  for (let i = 1; i < x + 1; i++) {
    res = res * i;
  }
  console.log(res);
}

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  factorial(parseInt(process.argv[2]));
}
