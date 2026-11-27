-- =====================================================
-- E-COMMERCE PAYMENT ANALYSIS
-- Database: PostgreSQL
-- =====================================================


-- 1. Analyze Total Revenue and Number of Payments by Payment Type

SELECT
    payment_type,
    ROUND(SUM(payment_value), 2) AS total_payment_value,
    COUNT(*) AS total_payments
FROM payments
GROUP BY payment_type
ORDER BY total_payment_value DESC;


-- 2. Calculate Average Payment Value by Payment Type

SELECT
    payment_type,
    ROUND(AVG(payment_value), 2) AS avg_payment_value,
    COUNT(*) AS total_payments
FROM payments
GROUP BY payment_type
ORDER BY avg_payment_value DESC;


-- 3. Calculate Payment Distribution by Payment Type

SELECT
    payment_type,
    COUNT(*) AS total_payments,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM payments),
        2
    ) AS payment_percentage
FROM payments
GROUP BY payment_type
ORDER BY payment_percentage DESC;


-- 4. Calculate Revenue Contribution by Payment Type

SELECT
    payment_type,
    ROUND(SUM(payment_value), 2) AS revenue_by_payment_method,
    ROUND(
        SUM(payment_value) * 100.0 /
        (SELECT SUM(payment_value) FROM payments),
        2
    ) AS revenue_percentage
FROM payments
GROUP BY payment_type
ORDER BY revenue_percentage DESC;


-- 5. Analyze Canceled Orders and Payment Values by Payment Type

SELECT
    p.payment_type,
    COUNT(DISTINCT o.order_id) AS canceled_orders,
    ROUND(SUM(p.payment_value), 2) AS total_payment_value
FROM orders o
JOIN payments p
    ON o.order_id = p.order_id
WHERE o.order_status = 'canceled'
GROUP BY p.payment_type
ORDER BY canceled_orders DESC;


-- 6. Calculate Cancellation Rate