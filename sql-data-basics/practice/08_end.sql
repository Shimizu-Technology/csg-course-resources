SELECT w.title, COALESCE(SUM(r.fee_cents), 0) AS confirmed_fee_cents
FROM workshops AS w
LEFT JOIN registrations AS r
  ON r.workshop_id = w.id AND r.status = 'confirmed'
GROUP BY w.id, w.title ORDER BY confirmed_fee_cents DESC, w.title;
