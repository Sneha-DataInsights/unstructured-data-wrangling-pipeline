
🏠 Unstructured Data Wrangling Pipeline

🚀 Overview

This project focuses on transforming highly unstructured housing data into a clean and structured dataset using Python.
The raw dataset contained fragmented multi-line records, inconsistent spacing, and embedded metadata, requiring custom data wrangling and parsing techniques.

❗ Challenges
-Multi-line fragmented records
-Irregular spacing instead of proper delimiters
-Missing and inconsistent values
-Non-tabular raw text structure

🧠 Solution Approach
-Loaded and filtered raw text data using Pandas
-Extracted column headers dynamically
-Reconstructed records split across multiple rows
-Applied Regular Expressions (Regex) for text parsing
-Performed data validation checks for nulls and duplicates
-Converted cleaned data into structured CSV format

📊 Exploratory Data Analysis (EDA)
-Performed basic EDA after cleaning the dataset:
-Correlation analysis
-Distribution visualization
-Relationship analysis between housing features and prices

Key Insight:
Properties with a higher average number of rooms (RM) showed a positive relationship with median house prices (MEDV).

🛠️ Tech Stack
-Python
-Pandas
-Matplotlib
-Seaborn
-Regular Expressions (Regex)

📂 Project Structure
-Plain text
-data/
 ├── unstructured_housing_data.txt
 ├── cleaned_housing_data.csv
-data_cleaning.ipynb
-data_cleaning_pipeline.py
-README.md

💡 Key Highlights
✔ Real-world messy data handling
✔ Multi-line record reconstruction
✔ Regex-based text parsing
✔ Data validation and preprocessing
✔ Exploratory Data Analysis (EDA)

👩‍💻 Author

Sneha
📧 sneha.2929sk@gmail.com
🔗 https://github.com/Sneha-DataInsights
