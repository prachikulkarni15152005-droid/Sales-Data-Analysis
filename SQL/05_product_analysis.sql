-- =====================================================
-- E-COMMERCE PRODUCT ANALYSIS
-- Database: PostgreSQL
-- =====================================================


-- 1. Analyze Total Revenue and Items Sold by Product Category

SELECT
    p.product_category_name_english AS product_category,
    ROUND(SUM(oi.price), 2) AS total_sales_revenue,
    COUNT(*) AS total_items_sold
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_category_name_english
ORDER BY total_sales_revenue DESC;


-- 2. Calculate Average Selling Price by Product Category

SELECT
    p.product_category_name_english AS product_category,
    ROUND(AVG(oi.price), 2) AS avg_selling_price,
    COUNT(*) AS total_order_items
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_category_name_english
ORDER BY avg_selling_price DESC;


-- 3. Identify Top-Performing Individual Products by Revenue

SELECT
    p.product_id,
    p.product_category_name_english AS product_category,
    ROUND(SUM(oi.price), 2) AS total_sales_revenue,
    COUNT(*) AS total_items_sold
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY
    p.product_id,
    p.product_category_name_english
ORDER BY total_sales_revenue DESC
LIMIT 10;


-- =====================================================
-- END OF PRODUCT ANALYSIS
-- =====================================================