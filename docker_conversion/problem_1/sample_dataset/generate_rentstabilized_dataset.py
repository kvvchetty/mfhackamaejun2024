import pandas as pd
import numpy as np

# Define number of data points
num_data_points = 10000

# Create lists for attributes
unit_ids = range(1, num_data_points + 1)
import random
import string

# Generate random fake addresses with different state codes
states = ['CA', 'TX', 'NY', 'FL', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI']
addresses = [f"{random.randint(1, 9999)} {random.choice(string.ascii_uppercase)} St, {random.choice(string.ascii_uppercase)}nytown, {random.choice(states)}" for i in range(1, num_data_points+1)]
# Create a pandas DataFrame with the generated data
# Use numpy.random.Generator for generating random numbers
rng = np.random.default_rng(seed=42)
num_units = rng.integers(10, 101, size=num_data_points)
building_types = rng.choice(["Apartment", "Townhouse"], size=num_data_points)
year_built = rng.integers(1950, 2025, size=num_data_points)
square_footage = rng.integers(100000, 500001, size=num_data_points)

# Generate random values for boolean and numeric attributes
rent_stabilization_status = rng.choice(["Yes", "No"], size=num_data_points, p=[0.6, 0.4])
delinquency_rate = rng.random(num_data_points) * 10
maintenance_cost = rng.integers(100, 300, size=num_data_points) * num_units
tenant_turnover_rate = rng.random(num_data_points) * 20
occupancy_rate = rng.random(num_data_points) * (1 - 0.1) + 0.1  # Ensure minimum occupancy
ltv = rng.random(num_data_points) * (1 - 0.2) + 0.2  # Ensure minimum equity
cap_rate = rng.random(num_data_points) * 0.15

# Combine data into a DataFrame
data = pd.DataFrame({
    "Multifamily Unit ID": unit_ids,
    "Address": addresses,
    "Number of Units": num_units,
    "Building Type": building_types,
    "Building Year Built": year_built,
    "Square Footage": square_footage,
    "Rent Stabilization Status": rent_stabilization_status,
    "Delinquency Rate": delinquency_rate,
    "Maintenance Cost": maintenance_cost,
    "Tenant Turnover Rate": tenant_turnover_rate,
    "Occupancy Rate": occupancy_rate,
    "LTV": ltv,
    "Cap Rate": cap_rate
    })
# Save data to Excel file

data.to_excel("rentstabilized_dataset.xlsx", index=False)

print(data)
    