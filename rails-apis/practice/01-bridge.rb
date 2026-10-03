def label(record)
  "#{record[:title]}: #{record[:capacity]} seats"
end
def total_seats(records)
  records.sum { |record| record[:capacity] }
end
puts label({ title: "Git practice", capacity: 6 })
puts total_seats([{ capacity: 6 }, { capacity: 4 }])
puts total_seats([])
