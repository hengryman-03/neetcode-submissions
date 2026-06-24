SELECT u.name,
       SUM(CASE WHEN r.distance IS NOT NULL THEN r.distance ELSE 0 END) AS travelled_distance
FROM Users u
LEFT JOIN Rides r ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC;