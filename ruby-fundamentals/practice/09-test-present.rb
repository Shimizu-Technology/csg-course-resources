def within_target?(minutes, target)
  minutes <= target
end
raise "below failed" unless within_target?(9, 10)
raise "equal failed" unless within_target?(10, 10)
raise "above failed" if within_target?(11, 10)
puts "3 boundary checks passed"
