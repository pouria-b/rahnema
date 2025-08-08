CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    created_at DATETIME
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    total_price REAL NOT NULL,
    created_at DATETIME,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

INSERT INTO users (id, name, created_at) VALUES
(1, 'Ali',  '2023-01-10 10:00:00'),
(2, 'Babak',    '2023-02-15 11:30:00'),
(3, 'Mahsa',  '2023-03-20 09:15:00'),
(4, 'Davod',  '2023-04-05 12:00:00'),
(5, 'Sina',    '2023-05-01 08:45:00');

INSERT INTO orders (id, user_id, total_price, created_at) VALUES
(101, 1, 120.50, '2023-01-15 14:00:00'),
(102, 2, 250.00, '2023-02-18 16:00:00'),
(103, 1, 75.00,  '2023-03-10 10:30:00'),
(104, 3, 180.25, '2023-03-22 12:45:00'),
(105, 1, 90.00,  '2023-06-01 09:00:00'),
(106, 4, 300.00, '2023-07-11 15:00:00'),
(107, 2, 100.00, '2023-08-01 11:00:00');


# query 1
SELECT
    u.id AS user_id,
    u.name,
    SUM(o.total_price) AS total_spent
FROM users u
JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
ORDER BY total_spent DESC
LIMIT 5;

# query 2
SELECT
    u.id AS user_id,
    u.name,
    u.created_at
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;

# query 3
WITH months AS (
    SELECT '2023-01' AS month UNION ALL
    SELECT '2023-02' UNION ALL
    SELECT '2023-03' UNION ALL
    SELECT '2023-04' UNION ALL
    SELECT '2023-05' UNION ALL
    SELECT '2023-06' UNION ALL
    SELECT '2023-07' UNION ALL
    SELECT '2023-08' UNION ALL
    SELECT '2023-09' UNION ALL
    SELECT '2023-10' UNION ALL
    SELECT '2023-11' UNION ALL
    SELECT '2023-12'
),
order_avg AS (
    SELECT
        strftime('%Y-%m', created_at) AS month,
        AVG(total_price) AS avg_order_price
    FROM orders
    WHERE strftime('%Y', created_at) = '2023'
    GROUP BY month
)
SELECT
    m.month,
    COALESCE(o.avg_order_price, 0) AS avg_order_price
FROM months m
LEFT JOIN order_avg o ON m.month = o.month
ORDER BY m.month;
