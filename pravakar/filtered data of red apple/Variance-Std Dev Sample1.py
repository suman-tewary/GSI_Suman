
import pandas as pd
import numpy as np

# Load the Excel file
file_path = 'D:\Spectra\Green Apple\Gsi_GreenApp.xlsx'  # Replace with the actual path to your Excel file
data = pd.read_excel(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Group by 'Day' and calculate the variance for each wavelength
grouped_data = data.groupby('Day').mean()  # Get the mean intensity for each day
variance_across_days = grouped_data.var()  # Calculate the variance across days

# Sort the variances in descending order
sorted_variance = variance_across_days.sort_values(ascending=False)

# Display the wavelengths with the highest variances
print("Top wavelengths by variance across days:")
print(sorted_variance.head(10))

# Optional: Save the variance data to a CSV file
output_path = 'variance_across_days.csv'
sorted_variance.to_csv(output_path, header=["Variance"])
print(f"Variance data saved to {output_path}")
