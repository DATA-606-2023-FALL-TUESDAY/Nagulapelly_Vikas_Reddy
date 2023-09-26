# Title and Author
- **Title:** Analysis of Used Cars and Price Prediction
- **Prepared for:** UMBC Data Science master’s degree Capstone by Dr. Chaojie (Jay) Wang
- **Author:** Vikas Reddy Nagulapelly
- **GitHub:** [https://github.com/vikas-reddy-319](https://github.com/vikas-reddy-319)
- **LinkedIn:** [https://www.linkedin.com/in/vikasreddynagulapelly](https://www.linkedin.com/in/vikasreddynagulapelly)

# Background
**Background:** Craigslist is one of the largest advertisement websites for viewing and posting local advertisements, covering various categories, including housing, job postings, items for sale, services, and personals. The data for this project was scraped from the website [Craigslist](https://www.craigslist.org).

**What is it about:** This project focuses on buying used cars and addresses a common issue with buying secondhand cars: the lack of control over pricing.

**Why does it matter:** Access to the right information can help anyone make informed decisions and find good deals when buying a car.

**Research Questions:**
1. Identify the trends in the sales of cars over the years.
2. Investigate the correlation between car price and its specifications.
3. Predict the price of a used car based on its specifications.

# Data
**Data Sources:** [https://github.com/AustinReese/UsedVehicleSearch](https://github.com/AustinReese/UsedVehicleSearch)

**Data Size:** 1.45 GB

**Data Shape:** 426,880 rows, 26 columns

**Time Period:** 1900 - 2022

**Columns Description and Data Types:**
- **ID (int):** Unique ID assigned to every ad and serves as the primary key.
- **Price (int):** Price in US dollars, not adjusted for inflation.
- **Year (float):** Year of car manufacture.
- **Manufacturer (string):** Name of the car manufacturer, with 43 unique businesses.
- **Model (string):** Exact model of the car.
- **Condition (string):** Condition of the car (e.g., excellent, good, fair, like new, salvage, new).
- **Cylinders (string):** Number of cylinders in the car engine (ranging from 3 to 12).
- **Fuel (string):** Type of fuel used (diesel, gas, electric, hybrid, other).
- **Odometer (float):** Distance the car has traveled after purchase.
- **Status (string):** Status of the car (clean, lien, rebuilt, salvage, parts only, missing).
- **Transmission (string):** Type of transmission (automatic, manual, other).
- **VIN (string):** Vehicle identification number.
- **Drive (string):** Drive transmission type (4WD, FWD, RWD).
- **Type (string):** Vehicle type (e.g., SUV, mini-van).
- **State (string):** Short form representation of the state where the car is listed.
- **Latitude, Longitude (float):** Geographic coordinates representing the car's location for sale.

