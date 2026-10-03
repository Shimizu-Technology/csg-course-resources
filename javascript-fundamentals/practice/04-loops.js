const prices = [12, 8, 15, 5];
let total = 0;
let overTen = 0;
for (const price of prices) {
  total += price;
  if (price > 10) overTen += 1;
  console.log("Running: " + total);
}
console.log("Total: " + total);
console.log("Over 10: " + overTen);
