def valid_break?(rest)
  rest.is_a?(Hash) && rest[:activity].is_a?(String) && !rest[:activity].strip.empty? && rest[:minutes].is_a?(Integer) && rest[:minutes] >= 0
end
def break_summary(breaks, target)
  raise ArgumentError, "invalid break" unless breaks.all? { |rest| valid_break?(rest) }
  total = breaks.sum { |rest| rest[:minutes] }
  groups = Hash.new(0)
  breaks.each { |rest| groups[rest[:activity]] += rest[:minutes] }
  longest = breaks.max_by { |rest| rest[:minutes] }
  lines = ["Total: #{total}"]
  groups.sort.each { |activity, minutes| lines << "#{activity}: #{minutes}" }
  if longest
    lines << "Longest: #{longest[:activity]} #{longest[:minutes]}"
  else
    lines << "Longest: none"
  end
  lines << "Difference: #{total - target}"
  lines.join("\n")
end
puts break_summary([{ activity: "Water", minutes: 5 }, { activity: "Walk", minutes: 8 }, { activity: "Water", minutes: 4 }], 20)
puts break_summary([], 20)
