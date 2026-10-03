function totalForArea(trips, area) {
  let total = 0;
  for (const trip of trips) {
    if (trip.area === area) total += trip.minutes;
  }
  return total;
}
const trips = [{ area: "Hagatna", minutes: 12 }, { area: "Dededo", minutes: 18 }];
console.log(totalForArea(trips, "Hagatna"));
console.log(totalForArea(trips, "Yigo"));
console.log(totalForArea([], "Hagatna"));
