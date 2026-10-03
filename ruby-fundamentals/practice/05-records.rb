breaks = [{ activity: "Water", minutes: 5 }, { activity: "Walk", minutes: 8 }, { activity: "Water", minutes: 4 }]
totals = Hash.new(0)
breaks.each do |rest|
  totals[rest[:activity]] += rest[:minutes]
end
p totals
puts "First: #{breaks[0][:activity]}"
