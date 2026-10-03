SELECT w.title, w.capacity - COUNT(r.id) AS open_seats
FROM workshops AS w
LEFT JOIN registrations AS r
  ON r.workshop_id = w.id AND r.status = 'confirmed'
GROUP BY w.id, w.title, w.capacity ORDER BY w.id;
