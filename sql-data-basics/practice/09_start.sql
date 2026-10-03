SELECT DISTINCT w.title FROM workshops AS w JOIN registrations AS r ON r.workshop_id = w.id WHERE r.status != 'confirmed' ORDER BY w.title;
