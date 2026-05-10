#!/usr/bin/node

let biggest = -Infinity;
let secondBiggest = -Infinity;

let i = 2;

while (process.argv[i] !== undefined) {
  const num = parseInt(process.argv[i]);

  if (num > biggest) {
    secondBiggest = biggest;
    biggest = num;
  } else if (num > secondBiggest) {
    secondBiggest = num;
  }

  i++;
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  console.log(secondBiggest);
}
