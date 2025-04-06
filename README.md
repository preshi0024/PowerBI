Blinkit Sales Data Dashboard: Technical Report
1. Introduction and Problem Statement
Blinkit, a rapidly expanding hyperlocal delivery network, competes fiercely in a market where quick delivery, satisfied customers, and effective marketing are key factors in a successful business. In order to maintain its growth and outperform rivals, Blinkit must:
• Recognize trends in sales over time and across product categories.
The Assess delivery performance to reduce delays and raise customer satisfaction optimize marketing efforts to maximize return on investment; and analyze customer sentiment and retention to improve services.
Goal: By combining several datasets, this Power BI dashboard aims to give a thorough understanding of Blinkit's operations and facilitate the data-driven decision-making to improve business performance.
2. Data Sources and Collection Methodology Data Sources:
I sourced the dataset from Kaggle : https://www.kaggle.com/datasets/akxiit/blinkit- sales-dataset
The analysis combines data from multiple sources to create a holistic view of business performance:
• blinkit_orders.csv: Contains order-level information (order ID, order date, customer ID, etc.).
• blinkit_order_items.csv: Detailed data on items within each order (product ID, quantity, price).
• blinkit_customers.csv: Customer information (customer ID, name, segment, region, etc.).
• blinkit_delivery_performance.csv: Delivery status and performance metrics.
• blinkit_inventory.csv and blinkit_inventoryNew.csv: Inventory-level information.
• blinkit_marketing_performance.csv: Campaign effectiveness and ROI.
• blinkit_customer_feedback.csv: Customer sentiment and feedback ratings.
Data Collection Methodology:
• Data was collected from Blinkit's transactional databases and campaign management systems.
• CSV files were imported into Power BI and cleansed using Power Query to handle missing values, standardize data formats, and merge necessary tables.
• Datasets were joined using primary and foreign keys to create a unified data model.
3. Data Model Design and Implementation Data Model Approach:
The data model was built using a star schema to optimize query performance and ensure scalability.
• Fact Tables:
o blinkit_orders – Main transactional data.
o blinkit_order_items – Item-level order details.
o blinkit_delivery_performance – Delivery status and timelines.
o blinkit_marketing_performance – Campaign ROI and conversion metrics.
• Dimension Tables:
o blinkit_customers – Customer demographics and segmentation. o blinkit_products – Product catalog.
o blinkit_inventory – Inventory and stock details.
Relationships and Joins:
• Orders linked to order items using order_id.
• Customers connected to orders using customer_id.
• Products joined with order items using product_id.
• Campaigns and sales data linked using campaign_name.
• Delivery performance associated with sales via order_id.
4. Visualization Approach and Tool Justification Why Power BI?
Power BI was chosen for its:

• Seamless Data Integration: Ability to handle large datasets efficiently.
• Advanced Calculations: DAX for complex KPIs and custom measures.
• Intuitive Dashboards: User-friendly interface with drill-down and interactivity options.
• Cross-Platform Availability: Easy sharing through Power BI Service.
Visualization Strategy:
Each page of the dashboard focuses on a specific business objective:
• Page 1: High-level business KPIs and sentiment analysis.
• Page 2: Temporal trends in sales over time (by day, month, and quarter).
• Page 3: Deep dive into category performance and sentiment-based metrics.
5. Documentation of Key Calculated Fields and DAX Measures
Key DAX Calculations:
Total Sales:
Total Sales = SUM(blinkit_order_items[Quantity] * blinkit_order_items[Unit Price])
Average Sales:
Average Sales = AVERAGE(blinkit_order_items[Quantity] * blinkit_order_items[Unit Price])
YoY Growth:
YoY Growth =
VAR PreviousYear = CALCULATE(SUM(blinkit_order_items[Sales]), DATEADD(blinkit_orders[Order Date], -1, YEAR))
RETURN
IF(ISBLANK(PreviousYear), BLANK(), (SUM(blinkit_order_items[Sales]) - PreviousYear) / PreviousYear)
Customer Retention Rate: Retention Rate = DIVIDE(
DISTINCTCOUNT(blinkit_orders[customer_id]),
CALCULATE(DISTINCTCOUNT(blinkit_orders[customer_id]), ALL(blinkit_orders)) )

Moving Average Sales (3-Month Rolling): 3M Moving Average Sales = AVERAGEX(
DATESINPERIOD( blinkit_orders[Order Date], MAX(blinkit_orders[Order Date]), -3,
MONTH
),
[Total Sales] )
6. Analysis of Findings and Insights
Page 1: Business Overview and Sentiment Analysis
Total Sales: Blinkit achieved 11.01M in total sales, with an average transaction size of 2.20K.
Customer Sentiment: Positive sentiment dominates, with a 3.34 average rating. Delays in delivery correlate with slightly lower ratings, emphasizing the need for delivery optimization.
Category Breakdown: High-performing categories include Dairy & Breakfast, Personal Care, and Grocery & Staples, driving more than 60% of total revenue.
Page 2: Temporal Sales Trends
Quarterly Trends: Consistent growth across quarters, with Q3 witnessing the highest sales volume.
Seasonal Peaks: November and December drive significant sales spikes due to festive periods.
Daily Trends: Periodic sales peaks suggest that promotions and weekend sales influence buying behavior.
Page 3: Deep Dive – Category and Sentiment Analysis
Sales by Category: Top-selling categories exhibit higher customer retention and positive sentiment.

Sentiment Impact: Positive sentiment correlates with higher average sales, whereas negative sentiment tends to reduce customer engagement.
Campaign Effectiveness: Campaigns that target high-margin categories yield better ROI, emphasizing the need to focus on premium product categories.
7. Challenges Encountered and Solutions Implemented
Data Quality and Cleansing:
Challenge: Inconsistent customer IDs and product data.
Solution: Used Power Query to standardize data formats and remove duplicates.
Handling Large Datasets:
Challenge: Performance lag with large CSV files.
Solution: Optimized relationships and used aggregations to improve report performance.
Delivery Delay Analysis:
Challenge: Difficulty in linking delay patterns to customer sentiment.
Solution: Created calculated fields to map sentiment scores to delivery status, revealing delivery delays as a key contributor to lower ratings.
8. Future Enhancements and Next Steps AI-Powered Predictive Models
• Use AI/ML models to forecast times of increased demand and possible supply delays.
• Project future sales patterns to minimize stockouts and maximize inventory.
Enhanced Campaign Attribution
• Use multi-touch attribution models to assess how different marketing channels affect sales conversions.

Conclusion
Blinkit has strong insights into sales, customer behavior, and campaign performance thanks to their Power BI dashboard. Blinkit is in a good position to increase customer satisfaction, optimize revenue, and keep its competitive edge in the hyperlocal delivery industry by resolving delivery inefficiencies, honing marketing tactics, and enhancing inventory management.
