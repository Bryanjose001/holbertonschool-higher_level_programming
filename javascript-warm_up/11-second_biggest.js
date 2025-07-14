#!/usr/bin/node
const args = process.argv.slice(2).map(x => parseInt(x));

if (args.length < 2) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a);

  const first = sorted[0];
  let second = null;

  for (let i = 1; i < sorted.length; i++) {
    if (sorted[i] !== first) {
      second = sorted[i];
      break;
    }
  }

  console.log(second === null ? 0 : second);
}
