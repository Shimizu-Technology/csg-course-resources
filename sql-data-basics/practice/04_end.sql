SELECT status, COUNT(*) AS registration_rows FROM registrations GROUP BY status ORDER BY status;
