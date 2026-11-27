# E-Commerce Sales Analysis Using SQL & Python

## Project Overview

This project focuses on analyzing e-commerce transactional data to uncover meaningful business insights related to sales performance, product categories, payment preferences, and customer purchasing behavior.

Using PostgreSQL and Python, the project involves data preparation, exploratory analysis, and business-focused SQL queries to identify trends and support data-driven decision-making.

## Project Objectives

- Analyze overall sales performance and revenue trends.
- Identify high-performing product categories and individual products.
- Evaluate customer payment preferences and payment distribution.
- Examine order cancellations across payment methods.
- Understand customer purchasing patterns and repeat purchases.
- Identify opportunities to improve customer retention.

## Tools & Technologies

- **Database:** PostgreSQL
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib
- **Development Environment:** Visual Studio Code, Jupyter Notebook
- **Version Control:** Git and GitHub

## Dataset

The project uses the Brazilian E-Commerce Public Dataset by Olist.

The dataset contains information about orders, customers, products, payments, reviews, sellers, and order items.

**Dataset Source:** [Brazilian E-Commerce Public Dataset by Olist – Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## Project Structure

```text
Ecommerce_Sales_Analysis/
│
├── Python/
│   ├── Data cleaning and analysis scripts
│   └── Exploratory data analysis scripts
│
├── SQL/
│   ├── 01_create_tables.sql
│   ├── 02_import_data.psql
│   ├── 03_sales_analysis.sql
│   ├── 04_payment_analysis.sql
│   ├── 05_product_analysis.sql
│   ├── 06_customer_analysis.sql
│   └── business_insights.md
│
├── data/
│   └── Dataset files
│
└── README.md
```

## Analysis Performed

### 1. Sales Analysis
- Total revenue calculation.
- Average Order Value (AOV).
- Monthly revenue and order trends.
- Month-over-Month (MoM) revenue growth using SQL window functions.

### 2. Payment Analysis
- Payment distribution by payment type.
- Average payment value.
- Revenue contribution by payment method.
- Order cancellation count and cancellation rate.

### 3. Product Analysis
- Revenue by product category.
- Total items sold by category.
- Average selling price by category.
- Top-performing individual products by revenue.

### 4. Customer Analysis
- Identification of repeat and one-time customers.
- Customer purchase frequency.
- Customer segmentation using SQL CASE statements.
- Revenue comparison between repeat and one-time customers.
- Repeat customer percentage.

## Key Business Insights

| Business Metric | Finding |
|---|---:|
| Total Product Revenue | R$13,591,643.70 |
| Total Orders Analyzed | 98,666 |
| Average Order Value | R$137.75 |
| Highest Revenue Category | Health & Beauty |
| Highest Revenue Month | November 2017 |
| Repeat Customer Percentage | 3.12% |

Additional findings and recommendations are documented in [`SQL/business_insights.md`](SQL/business_insights.md).

## Business Recommendations

- Develop customer retention strategies to encourage repeat purchases.
- Monitor high-performing product categories to identify growth opportunities.
- Investigate payment methods with higher cancellation rates.
- Track monthly revenue trends to support business planning.
- Use customer purchasing behavior to improve marketing strategies.

## How to Run the Project

1. Clone this repository:

   ```bash
   git clone https://github.com/prachikulkarni15152005-droid/Sales-Data-Analysis.git
   ```

2. Open the project in Visual Studio Code.

3. Set up PostgreSQL and create the required database.

4. Execute `SQL/01_create_tables.sql` to create the tables.

5. Import the dataset using the provided import script and your local dataset files.

6. Execute the SQL analysis scripts in the `SQL` folder.

7. Run the Python scripts for data cleaning and exploratory analysis.

## Important Notes

- Product revenue calculations use order item prices and exclude freight charges.
- Payment value and product revenue are different financial measures.
- The analysis includes all order statuses unless a query explicitly applies a status filter.
- Incomplete monthly periods should be considered when interpreting trends.
- Findings represent observed patterns in the available dataset and do not establish causal relationships.

## Author

**Prachi Kulkarni**

B.E. Artificial Intelligence and Machine Learning

Interested in Data Analytics, SQL, Python, and data-driven business insights.

[GitHub](https://github.com/prachikulkarni15152005-droid)