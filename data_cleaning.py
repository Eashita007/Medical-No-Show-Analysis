# data_cleaning.py

import pandas as pd

# Load the dataset
df = pd.read_csv('Dataset/KaggleV2-May-2016.csv')

# Rename columns for consistency
df.columns = [col.strip().lower().replace('-', '_') for col in df.columns]

# Convert date columns to datetime format
df['scheduledday'] = pd.to_datetime(df['scheduledday'])
df['appointmentday'] = pd.to_datetime(df['appointmentday'])

# Map 'No-show' to boolean
df['no_show'] = df['no_show'].map({'No': False, 'Yes': True})

# Convert binary columns to boolean
binary_columns = ['scholarship', 'hipertension', 'diabetes', 'alcoholism', 'sms_received']
df[binary_columns] = df[binary_columns].astype(bool)

# Remove duplicate row if any
df.drop_duplicates(inplace=True)

# Remove invalid age rows
df = df[df['age'] >= 0]

# Save cleaned dataset
df.to_csv('Dataset/cleaned_medical_appointments.csv', index=False)

print("✅ Data cleaning complete. Cleaned dataset saved to 'Dataset/cleaned_medical_appointments.csv'")
