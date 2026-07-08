# Production-Ready E-Commerce Data Extraction Pipeline

A robust, enterprise-grade Python web scraping pipeline designed to extract competitive pricing data from retail platforms seamlessly. Built with defensive programming practices to handle character encoding glitches and server rate limits automatically.

## 🚀 Business Value
Manual market research takes hours and is prone to human error. This automated tool extracts 1,000 product records across 50 pages in under a minute, delivering clean, structured data ready for immediate dynamic pricing analysis, market trend tracking, or business intelligence ingestion.

## 🛠️ Technical Features Built-In
* **Character Encoding Resiliency:** Utilizes regular expressions (`re`) to bypass common UTF-8/ISO-8859 text extraction glitches, ensuring clean numerical data types.
* **Polite Scraping Architecture:** Features an intentional 1-second delay loop (`time.sleep`) to respect target server bandwidth and prevent IP blacklisting.
* **Fault-Tolerant Parsing:** Wrapped in strategic `try-except` blocks so structural changes on an individual web element do not crash the entire long-running pipeline.
* **Automated Data Cleaning:** Converts raw HTML string metrics directly into structured floats and sanitized categorical strings before storage.

## 📊 Data Dictionary (Output Structure)
The script automates data cleaning and outputs a production-ready `scraped_market_data.csv` with the following schema:

| Column Name | Data Type | Description | Sample Value |
| :--- | :--- | :--- | :--- |
| **Title** | String | Full product name parsed from the DOM | *A Light in the Attic* |
| **Price_GBP** | Float | Cleaned numerical price for direct calculation | *51.77* |
| **Availability** | String | Cleaned stock status indicator | *In stock* |

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/lazy-laksh/ecommerce-price-scraper.git](https://github.com/lazy-laksh/ecommerce-price-scraper.git)