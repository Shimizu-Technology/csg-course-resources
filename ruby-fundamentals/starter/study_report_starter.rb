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
end

def report(sessions, goal)
  # TODO: combine the results into a readable summary.
end

puts report(SESSIONS, GOAL)
