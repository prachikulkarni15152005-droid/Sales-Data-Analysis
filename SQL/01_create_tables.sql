--checking current database--
SELECT current_database();
--create table orders--
CREATE TABLE orders (
    order_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50),
    order_status VARCHAR(30),
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
);
--verify order table--
SELECT *
FROM orders;
--checking any records present in orders--
SELECT COUNT(*)
FROM orders;
--checking records--
SELECT *
FROM orders
LIMIT 5;
--creating payments table--
CREATE TABLE payments (
    order_id VARCHAR(50),
    payment_sequential INTEGER,
    payment_type VARCHAR(30),
    payment_installments INTEGER,
    payment_value NUMERIC(12,2),
    PRIMARY KEY (order_id, payment_sequential)
);
--verify payments record--
SELECT COUNT(*)
FROM payments;
--craeting order_items table--
CREATE TABLE order_items (
    order_id VARCHAR(50),
    order_item_id INTEGER,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date TIMESTAMP,
    price NUMERIC(12,2),
    freight_value NUMERIC(12,2),
    PRIMARY KEY (order_id, order_item_id)
);
--verifying order_items record--
SELECT COUNT(*)
FROM order_items;
--creating products table --
CREATE TABLE products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_category_name VARCHAR(100),
    product_name_lenght INTEGER,
    product_description_lenght INTEGER,
    product_photos_qty INTEGER,
    product_weight_g NUMERIC(10,2),
    product_length_cm NUMERIC(10,2),
    product_height_cm NUMERIC(10,2),
    product_width_cm NUMERIC(10,2),
    product_category_name_english VARCHAR(100)
);
--altering the payments table--
ALTER TABLE products
ALTER COLUMN product_name_lenght TYPE NUMERIC(10,2),
ALTER COLUMN product_description_lenght TYPE NUMERIC(10,2),
ALTER COLUMN product_photos_qty TYPE NUMERIC(10,2);
--verifying products table--
SELECT COUNT(*)
FROM products;
--creating customers table --
CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix VARCHAR(5),
    customer_city VARCHAR(100),
    customer_state VARCHAR(5)
);
--verifying customers table--
SELECT COUNT(*)
FROM customers;
--creating sellers table --
CREATE TABLE sellers (
    seller_id VARCHAR(50) PRIMARY KEY,
    seller_zip_code_prefix VARCHAR(5),
    seller_city VARCHAR(100),
    seller_state VARCHAR(5)
);
--verifying sellers table--
SELECT COUNT(*)
FROM sellers;
--creating order_reviews table--
CREATE TABLE order_reviews (
    review_id VARCHAR(50),
    order_id VARCHAR(50),
    review_score INTEGER,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date TIMESTAMP,
    review_answer_timestamp TIMESTAMP,
    review_year INTEGER,
    review_month INTEGER,
    review_month_name VARCHAR(20),
    response_time_days NUMERIC(12,6)
);
--verifying order_reviews table--
SELECT COUNT(*)
FROM order_reviews;
--craeting category_tarnslation table--
CREATE TABLE category_translation (
    product_category_name VARCHAR(100),
    product_category_name_english VARCHAR(100)
);
--verifying category_translation table--
SELECT COUNT(*)
FROM category_translation;
--creating geolocation table--
CREATE TABLE geolocation (
    geolocation_zip_code_prefix VARCHAR(5),
    geolocation_lat NUMERIC(10,7),
    geolocation_lng NUMERIC(10,7),
    geolocation_city VARCHAR(100),
    geolocation_state VARCHAR(5),
    coordinate_flag VARCHAR(30)
);
--verifying geolocation table--
SELECT COUNT(*)
FROM geolocation;