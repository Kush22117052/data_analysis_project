# Zepto Inventory Data Analysis

## 📋 Project Overview

This project focuses on the **data exploration**, **cleaning**, and **analysis** of an e-commerce inventory dataset (`zepto`). The dataset includes product-level information such as pricing, discounts, availability, weight, and stock status. The goal is to uncover meaningful insights that can help in decision-making for pricing strategy, stock management, and revenue optimization.

---

## 🛠️ Table Schema

**Table Name:** `zepto`

| Column Name             | Data Type        | Description                                 |
|------------------------|------------------|---------------------------------------------|
| `sku_id`               | SERIAL (PK)      | Unique identifier for each product SKU      |
| `category`             | VARCHAR(120)     | Product category                            |
| `name`                 | VARCHAR(150)     | Product name                                |
| `mrp`                  | NUMERIC(8,2)     | Maximum Retail Price                        |
| `discountPercent`      | NUMERIC(5,2)     | Discount percentage                         |
| `availableQuantity`    | INTEGER          | Units currently available in inventory      |
| `discountedSellingPrice` | NUMERIC(8,2)   | Selling price after applying the discount   |
| `weightInGms`          | INTEGER          | Weight of the product in grams              |
| `outOfStock`           | BOOLEAN          | Whether the product is out of stock         |
| `quantity`             | INTEGER          | Ordered quantity (may be unused)            |

---

## 🔍 Data Exploration Queries

- **Row Count:** Total number of records.
- **Sample Records:** First 10 entries.
- **Null Checks:** Identify missing values across all fields.
- **Unique Categories:** List all distinct product categories.
- **Stock Status:** Count of products that are in stock vs. out of stock.
- **Duplicate Names:** Products listed under the same name multiple times.

---

## 🧹 Data Cleaning

- **Invalid Prices:** Identify and delete products with `mrp = 0`.
- **Unit Conversion:** Convert MRP and discounted price from paise to rupees.
- **Re-check Price Integrity:** Review prices after conversion.

---

## 📊 Data Analysis

### Q1. Top 10 Best-Value Products
- Based on the highest **discountPercent**.

### Q2. High MRP but Out of Stock Products
- Products priced above ₹300 that are currently unavailable.

### Q3. Estimated Revenue per Category
- Multiply available quantity by discounted price to estimate revenue.

### Q4. Premium Products with Low Discount
- Products with **MRP > ₹500** and **discount < 10%**.

### Q5. Top 5 Categories by Average Discount
- Categories offering the greatest average savings.

### Q6. Best Price-per-Gram Products
- For products weighing **100g or more**, sorted by best value (₹/g).

### Q7. Weight-Based Product Categories
- Classify as `Low` (<1kg), `Medium` (<5kg), `Bulk` (≥5kg).

### Q8. Total Inventory Weight per Category
- Estimate total weight by category: `weightInGms * availableQuantity`.

---

## 🧾 How to Use

1. Run the SQL script step-by-step in a PostgreSQL environment (or compatible SQL DBMS).
2. Make sure the data is properly inserted before running analysis queries.
3. Modify the thresholds (like MRP > 500) if needed for your use case.

---

## 📌 Notes

- Data types and assumptions (like paise to rupees conversion) are based on common retail practices.
- The `quantity` column is currently unused in most queries.
- Queries can be modularly reused in BI tools or Python/PowerBI dashboards.

---

## 📈 Outcome

This project enables stakeholders to:
- Optimize pricing and promotions.
- Manage inventory based on demand and weight.
- Focus on high-value or high-revenue-generating categories.

---

## 📁 File Structure

- `zepto_analysis.sql` – SQL script for table creation, cleaning, and analysis.
- `README.md` – Documentation (this file).

---

## 🙋‍♂️ Author

**Kushagra Kumar Sinha**  
Final year student, Electrical Engineering  
NIT Raipur

---

