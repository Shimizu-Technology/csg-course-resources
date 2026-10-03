SELECT w.title
FROM workshops AS w
LEFT JOIN registrations AS r
  ON r.workshop_id = w.id AND r.status = 'confirmed'
GROUP BY w.id, w.title
HAVING COUNT(r.id) = 0
ORDER BY w.title;
