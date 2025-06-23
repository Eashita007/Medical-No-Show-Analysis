# Medical No-Show Analysis

This repository contains data analysis on the "Medical Appointment No Shows" dataset from Kaggle.

## 📊 Dataset

- Source: [Kaggle](https://www.kaggle.com/datasets/joniarroba/noshowappointments)
- Location: `Dataset/KaggleV2-May-2016.csv`
- Size: 110,527 rows, 14 columns

## 🧹 Task 1: Data Cleaning and Preprocessing

### Cleaning Steps:
- Renamed columns to lowercase and used snake_case
- Converted date columns to `datetime` format
- Mapped `No-show` from `'No'/'Yes'` to `False/True`
- Converted binary features to Boolean (`True/False`)
- Removed duplicate row
- Removed one row with invalid age (`age < 0`)
- Saved cleaned data to: `Dataset/cleaned_medical_appointments.csv`

### Tools Used:
- Python
- Pandas

## ✅ Deliverables
- `Dataset/cleaned_medical_appointments.csv`
- `data_cleaning.py`
