# Ruby Fundamentals final project starter
# Run: ruby study_report_starter.rb
# Replace each TODO in order. Keep the sample data so your result can be checked.

SESSIONS = [
  { topic: "Ruby", minutes: 25 },
  { topic: "SQL", minutes: 20 },
  { topic: "Ruby", minutes: 35 },
  { topic: "Git", minutes: 15 },
  { topic: "SQL", minutes: 30 },
  { topic: "Ruby", minutes: 10 }
]
GOAL = 120

def valid_session?(session)
  # TODO: require a hash, a nonblank string topic, and nonnegative integer minutes.
end

def total_minutes(sessions)
  # TODO: add every session's minutes. An empty array should return 0.
end

def totals_by_topic(sessions)
  # TODO: return a hash of topic => total minutes.
end

def longest_session(sessions)
  # TODO: return the session with the most minutes, or nil if there are none.
end

def goal_status(total, goal)
  # TODO: return "under goal by N minutes", "on goal", or "over goal by N minutes".
  # Use "minute" for a difference of exactly 1.
end

def report(sessions, goal)
  # TODO: require an array and nonnegative integer goal; reject invalid sessions
  # using valid_session?, then combine results.
  # Raise ArgumentError for bad input; return a string, not printed output.
end

puts report(SESSIONS, GOAL)
