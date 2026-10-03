SELECT w.title, COUNT(r.id) AS confirmed
FROM workshops AS w
LEFT JOIN registrations AS r
  ON r.workshop_id = w.id AND r.status = 'confirmed'
GROUP BY w.id, w.title ORDER BY w.id;
