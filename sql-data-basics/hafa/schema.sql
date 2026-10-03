-- Fictional assessed workshop schema; use in Hafa schema.sql.
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
