import pandas as pd
import numpy as np

# 1. Load the dataset
# Replace 'your_file.csv' with the actual name of your file
print("Loading data...")
df = pd.read_csv('data.csv', low_memory=False)

print(f"Original Row Count: {len(df)}")

# ---------------------------------------------------------
# 2. Remove Nulls and Blanks
# ---------------------------------------------------------
# Convert empty strings or cells with only spaces to NaN
df.replace(r'^\s*$', np.nan, regex=True, inplace=True)

# Note: If you want to treat the text "Unknown" as a blank value, uncomment the next line:
df.replace('Unknown', np.nan, inplace=True)

# Drop rows where ANY column has a missing value
df.dropna(inplace=True)
print(f"Row Count after dropping nulls/blanks: {len(df)}")

# ---------------------------------------------------------
# 3. Clean Latitude and Longitude
df = df[
    (df['latitude'] > 6.0) & (df['latitude'] < 38.0) &
    (df['longitude'] > 68.0) & (df['longitude'] < 98.0)
]

# This print statement is accurate because the filter removed 0, -1, AND foreign coords
print(f"Row Count after cleaning coordinates (Removed 0, -1, and non-Indian locations): {len(df)}")

# ---------------------------------------------------------
# 4. Clean State Names (Keep only India)
# ---------------------------------------------------------

# A. Standardization Mapping
# Fixes variations like "NCT" -> "Delhi" and "Andaman and Nicobar" -> "Andaman and Nicobar Islands"
state_mapping = {
    'Andaman and Nicobar': 'Andaman and Nicobar Islands',  # Added as requested
    'NCT': 'Delhi',
    'NCT of Delhi': 'Delhi',
    'Orissa': 'Odisha',
    'Pondicherry': 'Puducherry',
    'Laccadives': 'Lakshadweep',
    'Uttaranchal': 'Uttarakhand',
    'Jammu and Kashmir': 'Jammu & Kashmir'
}

df['state_name'] = df['state_name'].replace(state_mapping)

# B. Allow-List (White List)
# Any state NOT in this list (like Bangkok, California, etc.) will be dropped.
valid_indian_states = [
    'Andaman and Nicobar Islands', 
    'Andhra Pradesh', 
    'Arunachal Pradesh', 
    'Assam', 
    'Bihar', 
    'Chandigarh', 
    'Chhattisgarh', 
    'Dadra and Nagar Haveli',
    'Dadra and Nagar Haveli and Daman and Diu', 
    'Daman and Diu', 
    'Delhi', 
    'Goa', 
    'Gujarat', 
    'Haryana', 
    'Himachal Pradesh', 
    'Jammu & Kashmir', 
    'Jharkhand', 
    'Karnataka', 
    'Kerala', 
    'Ladakh', 
    'Lakshadweep', 
    'Madhya Pradesh', 
    'Maharashtra', 
    'Manipur', 
    'Meghalaya', 
    'Mizoram', 
    'Nagaland', 
    'Odisha', 
    'Puducherry', 
    'Punjab', 
    'Rajasthan', 
    'Sikkim', 
    'Tamil Nadu', 
    'Telangana', 
    'Tripura', 
    'Uttar Pradesh', 
    'Uttarakhand', 
    'West Bengal'
]

# Keep only rows that exist in the valid list
df = df[df['state_name'].isin(valid_indian_states)]

print(f"Final Row Count after removing foreign states: {len(df)}")

# ---------------------------------------------------------
# 5. Export
# ---------------------------------------------------------
print("Saving cleaned file...")
df.to_csv('Cleaned_Telecom_Data.csv', index=False)
print("Done! File saved as 'Cleaned_Telecom_Data.csv'")