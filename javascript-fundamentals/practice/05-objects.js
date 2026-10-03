const trips = [{ area: "Hagatna", minutes: 12 }, { area: "Dededo", minutes: 18 }, { area: "Hagatna", minutes: 8 }];
const totals = {};
for (const trip of trips) {
  const area = trip.area;
  totals[area] = (totals[area] ?? 0) + trip.minutes;
}
console.log(JSON.stringify(totals));
