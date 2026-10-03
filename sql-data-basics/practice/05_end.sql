SELECT w.title, r.status
FROM workshops AS w
JOIN registrations AS r ON r.workshop_id = w.id
WHERE r.id = 1;
