🏠 Unstructured Data Wrangling Pipeline

🚀 Overview

This project focuses on solving a real-world data problem by transforming highly unstructured housing data into a clean and structured format using Python.

Unlike standard datasets, the raw data was not in tabular form and required custom logic for parsing and reconstruction.



❗ Problem

The dataset contained multiple challenges:

- Records split across multiple rows
- Irregular spacing instead of proper delimiters
- Embedded metadata and noisy rows
- No predefined column structure

This made the dataset unsuitable for direct analysis.



🧠 Solution Approach

- Loaded raw text data and skipped invalid rows
- Dynamically extracted column headers
- Identified that each record spans across two rows
- Reconstructed complete records by merging split rows
- Used regex-based splitting to handle inconsistent spacing
- Converted raw text into structured tabular format



🛠️ Tech Stack

- Python
- Pandas
- Regex



📂 Project Structure

data/
 ├── unstructured_housing_data.txt
 ├── cleaned_housing_data.csv

data_cleaning_pipeline.py
data_cleaning.ipynb
data_cleaning_pipeline.html
README.md


📊 Outcome

- Successfully transformed messy raw data into structured dataset
- Improved data usability for analysis
- Demonstrated real-world data wrangling skills


💼 Key Highlight

This project demonstrates the ability to handle real-world messy data and build custom parsing solutions instead of relying on pre-cleaned datasets.


👩‍💻 Author

Sneha
📧 sneha.2929sk@gmail.com
🔗 https://github.com/Sneha-DataInsights
