#!/usr/bin/node
function factorial (x) {
  let res = 1;
  while (x > 1) {
    res = res * x;
    x = x - 1;
  }
  console.log(res);
}

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  factorial(process.argv[2]);
}
