def break_total(breaks)
  total = 0
  breaks.each { |rest| total += rest[:minutes] }
  total
end
puts break_total([{ minutes: 5 }, { minutes: 8 }])
puts break_total([])
puts break_total([{ minutes: 0 }])
