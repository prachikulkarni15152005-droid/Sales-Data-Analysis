# E-Commerce Sales Analysis – Business Insights

## 1. Project Overview

Analyzed e-commerce transactional data using PostgreSQL to identify sales trends, product performance, payment preferences, and customer purchasing behavior.

## 2. Payment Analysis

- Credit cards contributed **78.34%** of total payment value.
- Credit cards accounted for **73.92%** of payment records.
- Credit cards had the highest average payment value of **R$163.32**.
- Voucher payments recorded a cancellation rate of **2.43%**, higher than other major payment methods.

**Business Insight:** Credit cards are the dominant payment method in both transaction volume and payment value. Voucher cancellations may warrant further investigation.

## 3. Product Category Analysis

- Health & Beauty generated the highest revenue of **R$1,258,681.34**.
- Watches & Gifts ranked second, generating **R$1,205,005.68**.
- Bed Bath & Table recorded the highest sales volume with **11,115 items sold**.
- Computers had the highest average selling price of **R$1,098.34**.

**Business Insight:** Health & Beauty leads in revenue, while Bed Bath & Table leads in item volume. These categories demonstrate different sales-performance strengths.

## 4. Overall Sales Performance

- Total product revenue: **R$13,591,643.70**
- Total orders analyzed: **98,666**
- Average Order Value (AOV): **R$137.75**

**Business Insight:** The overall AOV provides a baseline for evaluating future changes in customer spending and order value.

## 5. Monthly Revenue Trends

- November 2017 recorded the highest monthly revenue of **R$1,010,271.37**.
- Revenue generally increased during 2017 and remained relatively strong during early 2018.
- September 2018 showed only one recorded order, indicating an incomplete period.

**Business Insight:** November 2017 was the strongest observed month. Incomplete months should be excluded from fair month-to-month performance comparisons.

## 6. Customer Purchase Analysis

- Total unique customers: **96,096**
- Repeat customers: **2,997 (3.12%)**
- One-time customers: **93,099 (96.88%)**
- Revenue from one-time customers: **R$12,812,821.73**
- Revenue from repeat customers: **R$778,821.97**

**Business Insight:** Most customers made only one purchase in the available dataset, highlighting an opportunity to improve repeat purchasing behavior.

## 7. Customer Retention Insights

- Repeat customers generated approximately **1.88 times more revenue per customer** than one-time customers in this analysis.
- The observed repeat-purchase percentage was **3.12%**.

**Business Insight:** Customer loyalty programs, personalized promotions, and post-purchase engagement could help encourage repeat purchases.

## 8. Business Recommendations

1. Introduce customer retention campaigns to encourage repeat purchases.
2. Monitor high-revenue product categories and their sales performance.
3. Investigate payment methods associated with higher cancellation rates.
4. Track monthly revenue and order trends to identify changes in business performance.

## 9. Analysis Notes

- Product revenue is calculated using order item prices and excludes freight charges.
- Payment value and product revenue represent different financial measures.
- Unless explicitly filtered, the analysis includes all order statuses.
- Incomplete periods should be considered when interpreting monthly trends.
- Findings represent observed patterns and do not establish causal relationships.