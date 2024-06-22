import matplotlib.pyplot as plt
import numpy as np

# Sample data
rent_stabilization_levels = [2, 4, 6, 8]
lending_interest_rates = [3.5, 3.8, 4.2, 4.5]
loan_to_value_ratios = [0.8, 0.75, 0.7, 0.65]
transaction_volumes = [150, 130, 120, 110]
property_values = [200000, 195000, 190000, 185000]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot lending interest rates
plt.plot(rent_stabilization_levels, lending_interest_rates, marker='o', color='b', label='Lending Interest Rates')

# Plot loan-to-value ratios
plt.plot(rent_stabilization_levels, loan_to_value_ratios, marker='s', color='g', label='Loan-to-Value Ratios')

# Plot transaction volumes
plt.plot(rent_stabilization_levels, transaction_volumes, marker='^', color='r', label='Transaction Volumes')

# Plot property values
plt.plot(rent_stabilization_levels, property_values, marker='d', color='m', label='Property Values')

# Add labels and title
plt.xlabel('Rent Stabilization Percentages (%)')
plt.ylabel('Impact on Lending and Market Makers')
pltMultiplier = 1000
plt.title(f'What-If Analysis: Rent Stabilization Impact\n(Sample Data, n={pltMultiplier})')

# Add legend
plt.legend()

# Show grid
plt.grid(True)

# Show the plot
plt.show()
