-- Write your query below
SELECT name FROM customers
WHERE name NOT IN 
    (SELECT name FROM customers c JOIN orders o ON c.id = o.customer_id)