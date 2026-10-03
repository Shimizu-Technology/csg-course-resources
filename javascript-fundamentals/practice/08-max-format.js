function largestReading(readings) {
  if (readings.length === 0) return null;
  let largest = readings[0];
  for (const reading of readings) {
    if (reading.degrees > largest.degrees) largest = reading;
  }
  return largest;
}
function readingReport(readings) {
  const largest = largestReading(readings);
  const lines = ["Readings: " + readings.length];
  if (largest === null) lines.push("Largest: none");
  else lines.push("Largest: " + largest.area + " (" + largest.degrees + ")");
  return lines.join("\n");
}
console.log(readingReport([{ area: "Hagatna", degrees: 27 }, { area: "Yigo", degrees: 29 }, { area: "Dededo", degrees: 28 }]));
console.log(readingReport([]));
