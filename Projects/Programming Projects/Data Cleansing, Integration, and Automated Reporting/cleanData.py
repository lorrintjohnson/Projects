import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the path to the datasets folder
data_path = os.path.join(os.getcwd(), 'datasets')

# Load datasets from their respective subfolders
client_data = pd.read_csv(os.path.join(data_path, 'powerco_data', 'client_data.csv'))
price_data = pd.read_csv(os.path.join(data_path, 'powerco_data', 'price_data.csv'))
weather_data = pd.read_csv(os.path.join(data_path, 'weather_data', 'weather_data.csv'))
customer_service_data = pd.read_csv(os.path.join(data_path, 'customer_data', 'nys_utility_company_customer_service_response_data.csv'))
world_energy_data = pd.read_csv(os.path.join(data_path, 'world_energy_data', 'world_energy_data.csv'))

# Clean data
client_data.drop_duplicates(inplace=True)
price_data.ffill(inplace=True)

# Check if 'Service Provider' exists in customer_service_data
if 'Service Provider' in customer_service_data.columns:
    customer_service_data.dropna(subset=['Service Provider'], inplace=True)
else:
    print("Error: 'Service Provider' column not found in customer_service_data")
    print("Available columns:", customer_service_data.columns)

# Convert date columns to datetime format
client_data['date_activ'] = pd.to_datetime(client_data['date_activ'], errors='coerce')
weather_data['Date'] = pd.to_datetime(weather_data['Date'], format='%m/%d/%Y', errors='coerce')
world_energy_data['Dates'] = pd.to_datetime(world_energy_data['Dates'], errors='coerce')
customer_service_data['Date'] = pd.to_datetime(customer_service_data['Date'], format='%m/%d/%Y', errors='coerce')

# Extract year for merging
client_data['year'] = client_data['date_activ'].dt.year
weather_data['year'] = weather_data['Date'].dt.year
customer_service_data['year'] = customer_service_data['Date'].dt.year

# Calculate national average temperature by year for all locations
national_avg_temp = weather_data.groupby('year')['Temperature_F'].mean().reset_index()

# Merge datasets on year
combined_data = pd.merge(client_data, national_avg_temp, on='year', how='outer')

# Only merge customer_service_data if relevant columns exist
if 'Service Provider' in customer_service_data.columns:
    combined_data = pd.merge(combined_data, customer_service_data, left_on='id', right_on='Service Provider', how='outer')

# Ensure 'year' column is present in combined_data
if 'year' not in combined_data.columns:
    combined_data['year'] = combined_data['date_activ'].dt.year

# Automated Reporting
combined_data['date_end'] = pd.to_datetime(combined_data['date_end'], errors='coerce')
price_data['price_date'] = pd.to_datetime(price_data['price_date'], errors='coerce')

# 1. Line Chart: National Energy Consumption and Temperature
yearly_usage_weather = combined_data.groupby('year').agg({'imp_cons': 'sum', 'Temperature_F': 'mean'}).dropna()

fig, ax1 = plt.subplots(figsize=(8, 5))

ax1.set_xlabel('Year')
ax1.set_ylabel('Consumption (imp_cons)', color='tab:blue')
ax1.plot(yearly_usage_weather.index.astype(int), yearly_usage_weather['imp_cons'], color='tab:blue', label='Consumption (imp_cons)')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Temperature (°F)', color='tab:orange')
ax2.plot(yearly_usage_weather.index.astype(int), yearly_usage_weather['Temperature_F'], color='tab:orange', label='Temperature (°F) (Temperature_F)')
ax2.tick_params(axis='y', labelcolor='tab:orange')

fig.tight_layout()
plt.title('National Energy Consumption and Temperature')
plt.xticks(rotation=45)
plt.savefig('national_energy_consumption_and_temperature.png')
plt.show()

# 2. Line Chart: Energy Consumption and Customer Service Complaints
combined_complaints_consumption = pd.merge(client_data, customer_service_data, left_on='year', right_on='year', how='outer')
yearly_complaints_consumption = combined_complaints_consumption.groupby('year').agg({'imp_cons': 'sum', 'Complaint Response Time': 'mean'}).dropna()

fig, ax1 = plt.subplots(figsize=(8, 5))

ax1.set_xlabel('Year')
ax1.set_ylabel('Consumption (imp_cons)', color='tab:blue')
ax1.plot(yearly_complaints_consumption.index.astype(int), yearly_complaints_consumption['imp_cons'], color='tab:blue', label='Consumption (imp_cons)')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Complaint Response Time', color='tab:orange')
ax2.plot(yearly_complaints_consumption.index.astype(int), yearly_complaints_consumption['Complaint Response Time'], color='tab:orange', label='Complaint Response Time (Complaint Response Time)')
ax2.tick_params(axis='y', labelcolor='tab:orange')

fig.tight_layout()
plt.title('Energy Consumption and Customer Service Complaints')
plt.xticks(rotation=45)
plt.savefig('energy_consumption_and_customer_service_complaints.png')
plt.show()

# 3. Line Chart: National Energy Consumption vs Production
world_energy_production_consumption = world_energy_data.groupby(world_energy_data['Dates'].dt.year).agg({'Total Energy Production (qBtu)': 'sum', 'Total Energy Consumption (qBtu)': 'sum'}).dropna()

fig, ax1 = plt.subplots(figsize=(8, 5))

ax1.set_xlabel('Year')
ax1.set_ylabel('Total Energy Production (qBtu)', color='tab:blue')
ax1.plot(world_energy_production_consumption.index.astype(int), world_energy_production_consumption['Total Energy Production (qBtu)'], color='tab:blue', label='Total Energy Production (qBtu) (Total Energy Production (qBtu))')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Total Energy Consumption (qBtu)', color='tab:orange')
ax2.plot(world_energy_production_consumption.index.astype(int), world_energy_production_consumption['Total Energy Consumption (qBtu)'], color='tab:orange', label='Total Energy Consumption (qBtu) (Total Energy Consumption (qBtu))')
ax2.tick_params(axis='y', labelcolor='tab:orange')

fig.tight_layout()
plt.title('National Energy Consumption vs Production')
plt.xticks(rotation=45)
plt.savefig('national_energy_consumption_vs_production.png')
plt.show()
