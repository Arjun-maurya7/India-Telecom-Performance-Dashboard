# 📡 Telecom Call Quality Analysis Dashboard (India)
<img width="1660" height="928" alt="image" src="https://github.com/user-attachments/assets/be802cb0-1200-44ea-b818-51e411c8bf33" />


## 📊 Project Overview
This project analyzes the performance of major Indian telecom operators (Jio, Airtel, Vi, BSNL) to identify regions with high call drop rates and poor voice quality. The dashboard helps in diagnosing network issues across Indoor, Outdoor, and Travelling scenarios.

## 🛠️ Tech Stack
*   **Tool:** Microsoft Power BI Desktop
*   **Language:** DAX (Data Analysis Expressions)
*   **Data Source:** Data.gov.in (Indian Government Open Data)
*   **Design:** Custom Dark Theme / Glassmorphism UI

## 🔍 Key Insights & Features
*   **Market Share Analysis:** Visualized operator dominance (Jio vs. Competitors).
*   **Dynamic Matrix:** Heatmap showing critical failure zones by State & Operator.
*   **Defect Scoring:** Custom "Quality Score" algorithm to rank network performance.
*   **Time Trend:** Analyzed the impact of 5G rollout on call stability (2022-2024).

## 🚀 How to View
Download the `.pbix` file to view the full interactive dashboard.

## 🚀 How to Run Locally

1.  **Clone the repo:** `git clone https://github.com/Arjun-maurya7/India-Telecom-Performance-Dashboard`
2.  **Get API Key:** specific to the [Voice Call Quality dataset](https://www.data.gov.in/resource voice-call-quality-customer-experience-till-last-month).
3.  **Scrape:** Paste your API key inside `Data/scaping_data.py` and run the script.
4.  **Process:** Run `clean.py` to clean and format the dataset.
5.  **Visualize:** Open the Power BI project file and connect it to the cleaned data source.