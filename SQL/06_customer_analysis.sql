-- =====================================================
-- E-COMMERCE CUSTOMER ANALYSIS
-- Database: PostgreSQL
-- =====================================================


-- 1. Identify Repeat Customers and Their Order Counts

SELECT
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY c.customer_unique_id
HAVING COUNT(DISTINCT o.order_id) > 1
ORDER BY total_orders DESC;


-- 2. Calculate Total Number of Repeat Customers

WITH repeat_customers AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    GROUP BY c.customer_unique_id
    HAVING COUNT(DISTINCT o.order_id) > 1
)
SELECT
    COUNT(*) AS total_repeat_customers
FROM repeat_customers;


-- 3. Calculate Total Number of Unique Customers

SELECT
    COUNT(DISTINCT customer_unique_id) AS total_unique_customers
FROM customers;


-- 4. Calculate Total Number of One-Time Customers

WITH one_time_customers AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    GROUP BY c.customer_unique_id
    HAVING COUNT(DISTINCT o.order_id) = 1
)
SELECT
    COUNT(*) AS total_one_time_customers
FROM one_time_customers;


-- 5. Analyze Revenue by Customer Type

WITH customer_order_counts AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
),
customer_segments AS (
    SELECT
        customer_unique_id,
        CASE
            WHEN total_orders > 1 THEN 'Repeat'
            ELSE 'One-time'
        END AS customer_type
    FROM customer_order_counts
),
order_customer_segments AS (
    SELECT
        o.order_id,
        cs.customer_unique_id,
        cs.customer_type
    FROM orders o
    JOIN customers c
        ON o.customer_id = c.customer_id
    JOIN customer_segments cs
        ON c.customer_unique_id = cs.customer_unique_id
)
SELECT
    ocs.customer_type,
    COUNT(DISTINCT ocs.customer_unique_id) AS total_customers,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    ROUND(SUM(oi.price), 2) AS total_revenue
FROM order_customer_segments ocs
JOIN order_items oi
    ON ocs.order_id = oi.order_id
GROUP BY ocs.customer_type
ORDER BY total_revenue DESC;


-- 6. Calculate Repeat and One-Time Customer Percentages

WITH customer_order_counts AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS total_orders
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_unique_id
)
SELECT
    COUNT(*) AS total_unique_customers,
    COUNT(CASE
        WHEN total_orders > 1 THEN 1
    END) AS repeat_customers,
    COUNT(CASE
        WHEN total_orders = 1 THEN 1
    END) AS one_time_customers,
    ROUND(
        COUNT(CASE
            WHEN total_orders > 1 THEN 1
        END) * 100.0 / COUNT(*),
        2
    ) AS repeat_customer_percentage,
    ROUND(
        COUNT(CASE
            WHEN total_orders = 1 THEN 1
        END) * 100.0 / COUNT(*),
        2
    ) AS one_time_customer_percentage
FROM customer_order_counts;


-- =====================================================
-- END OF CUSTOMER ANALYSIS
-- =====================================================