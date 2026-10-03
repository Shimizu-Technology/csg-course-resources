function firstName(records) {
  if (records.length === 0) return "none";
  return records[0].name;
}
console.log(firstName([{ name: "Practice" }]));
console.log(firstName([]));
