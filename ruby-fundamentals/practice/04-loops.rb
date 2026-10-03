total = 0
over_twenty = 0
[25, 20, 35].each do |minutes|
  total += minutes
  over_twenty += 1 if minutes > 20
  puts "Running: #{total}"
end
puts "Total: #{total}"
puts "Over 20: #{over_twenty}"
