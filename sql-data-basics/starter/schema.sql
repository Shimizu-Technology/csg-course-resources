-- Fictional training data. Run with: python3 sql_starter.py
CREATE TABLE workshops (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  category TEXT NOT NULL,
  capacity INTEGER NOT NULL CHECK (capacity >= 0)
);
CREATE TABLE registrations (
  id INTEGER PRIMARY KEY,
  workshop_id INTEGER NOT NULL REFERENCES workshops(id),
  status TEXT NOT NULL CHECK (status IN ('confirmed', 'waitlisted', 'cancelled')),
  fee_cents INTEGER NOT NULL CHECK (fee_cents >= 0)
);
INSERT INTO workshops VALUES
  (1, 'Python Basics', 'code', 4),
  (2, 'SQL Basics', 'data', 3),
  (3, 'Web Intro', 'code', 5),
  (4, 'Git Basics', 'tools', 2);
INSERT INTO registrations VALUES
  (1, 1, 'confirmed', 2000),
  (2, 1, 'confirmed', 2000),
  (3, 1, 'waitlisted', 2000),
  (4, 2, 'confirmed', 3000),
  (5, 2, 'confirmed', 3000),
  (6, 2, 'confirmed', 3000),
  (7, 3, 'confirmed', 1500),
  (8, 3, 'cancelled', 1500);
