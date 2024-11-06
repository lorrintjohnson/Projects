# Data Cleansing, Integration, and Automated Reporting 

## Overview
In this project, I performed data cleansing, integration, and automated reporting using multiple datasets related to energy consumption, weather data, and customer service responses. The goal was to create a comprehensive data analysis pipeline that provides valuable insights through automated reports.

## Scenario
As a data analyst, I was tasked with integrating various datasets to analyze energy consumption patterns, correlate them with weather conditions, and assess customer service performance. The project involved cleaning and merging data from different sources and automating the generation of insightful reports.

## Steps Taken
1. **Data Collection**:
   - Gathered datasets from various sources, including customer service response data, energy consumption data, weather data, and national energy consumption data:
     - NYS Utility Company Customer Service Response Data (kaggle.com)
     - PowerCO (kaggle.com)
     - U.S. Energy and Indicators Dataset (1990-2025) (kaggle.com)
     - Climate at a Glance | Statewide Time Series | National Centers for Environmental Information (NCEI) (noaa.gov)
   - Organized the datasets into respective subfolders for easy access.

2. **Data Cleansing**:
   - Loaded the datasets into Python using pandas.
   - Inspected the data for missing values, duplicates, and inconsistencies.
   - Cleaned the data by removing duplicates and filling missing values.

3. **Data Integration**:
   - Merged the client and price data on `id`.
   - Integrated the merged data with weather data on `date_activ`.
   - Combined the resulting dataset with customer service data on `id`.

4. **Automated Reporting**:
   - Converted the `date_activ` column to datetime format.
   - Generated monthly energy usage reports and customer service response time reports using matplotlib.
   - Automated the report generation process using a task scheduler.

## Charts Created
1. **National Energy Consumption and Temperature**
   - **Description**: This line chart shows the yearly national energy consumption (`imp_cons`) and the national average temperature (`Temperature_F`) over time.
   - **File**: `national_energy_consumption_and_temperature.png`
   - **Result**: The chart indicates a trend in national energy consumption and temperature over the years.

2. **Energy Consumption and Customer Service Complaints**
   - **Description**: This line chart shows the yearly energy consumption (`imp_cons`) compared to customer service complaint response time (`Complaint Response Time`) over time.
   - **File**: `energy_consumption_and_customer_service_complaints.png`
   - **Result**: The chart provides insights into the relationship between energy consumption and customer service complaint response time over the years.

3. **National Energy Consumption vs Production**
   - **Description**: This line chart shows the yearly national energy production (`Total Energy Production (qBtu)`) compared to national energy consumption (`Total Energy Consumption (qBtu)`) over time.
   - **File**: `national_energy_consumption_vs_production.png`
   - **Result**: The chart highlights the trends in national energy production and consumption over the years.

## Conclusion
The project successfully demonstrated the ability to clean, integrate, and analyze data from multiple sources. The automated reports provided valuable insights into energy consumption patterns, weather conditions, and customer service performance. Key findings include:

- A clear trend in national energy consumption and temperature over time.
- Insights into the relationship between energy consumption and customer service complaint response time over the years.
- Trends in national energy production and consumption over time.

**Skills Demonstrated**
- Data stewardship
- ETL processes
- Data quality management
- Report automation
- Python scripting 

These insights showcase the effectiveness of the data analysis pipeline in providing valuable information for decision-making.
