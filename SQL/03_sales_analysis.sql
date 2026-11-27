-- =====================================================
-- E-COMMERCE SALES ANALYSIS
-- Database: PostgreSQL
-- =====================================================


-- 1. Calculate Total Revenue, Total Orders, and Average Order Value (AOV)

SELECT
    ROUND(SUM(oi.price), 2) AS total_revenue,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(
        SUM(oi.price) / COUNT(DISTINCT o.order_id),
        2
    ) AS average_order_value
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id;


-- 2. Analyze Monthly Revenue and Order Trends

SELECT
    TO_CHAR(o.order_purchase_timestamp, 'YYYY-MM') AS order_month,
    ROUND(SUM(oi.price), 2) AS monthly_revenue,
    COUNT(DISTINCT o.order_id) AS monthly_orders
FROM order_items oi
JOIN orders o
    ON oi.order_id = o.order_id
GROUP BY TO_CHAR(o.order_purchase_timestamp, 'YYYY-MM')
ORDER BY order_month;


-- 3. Calculate Month-over-Month (MoM) Revenue Growth

WITH monthly_sales AS (
    SELECT
        TO_CHAR(o.order_purchase_timestamp, 'YYYY-MM') AS order_month,
        SUM(oi.price) AS monthly_revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY TO_CHAR(o.order_purchase_timestamp, 'YYYY-MM')
),
revenue_comparison AS (
    SELECT
        order_month,
        monthly_revenue,
        LAG(monthly_revenue) OVER (
            ORDER BY order_month
        ) AS previous_month_revenue
    FROM monthly_sales
)
SELECT
    order_month,
    ROUND(monthly_revenue, 2) AS monthly_revenue,
    ROUND(previous_month_revenue, 2) AS previous_month_revenue,
    ROUND(
        monthly_revenue - previous_month_revenue,
        2
    ) AS revenue_difference,
    ROUND(
        (monthly_revenue - previous_month_revenue)
        * 100.0 / NULLIF(previous_month_revenue, 0),
        2
    ) AS mom_growth_percentage
FROM revenue_comparison
ORDER BY order_month;


-- =====================================================
-- END OF SALES ANALYSIS
-- =====================================================