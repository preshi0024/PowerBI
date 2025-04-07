Import necessary libraries
import os
import pandas as pd
import numpy as np
import glob
import random
from datetime import datetime

# Define a function to check and unify data types across multiple files
def unify_data_types(file_list):
    column_types = {}
    
    # Loop through all files to identify consistent data types
    for file in file_list:
        df = pd.read_csv(file)
        if df.empty:
            print(f"Warning: File {file} is empty and will be skipped.")
            continue
        for col in df.columns:
            if col in column_types:
                # Check if column type matches previous types
                if df[col].dtype != column_types[col]:
                    print(f"Warning: Column '{col}' in {file} has inconsistent data type! Expected {column_types[col]}, but got {df[col].dtype}.")
            else:
                column_types[col] = df[col].dtype
    
    # Return unified data types
    return column_types


# Function to clean and format date columns
def format_date_columns(df):
    for col in df.columns:
        if df[col].dtype == 'object':  # Only check string/object columns
            try:
                # Try parsing as date using infer_datetime_format
                df[col] = pd.to_datetime(df[col], errors='coerce', infer_datetime_format=True)
                # Fill nulls if any parsing errors occurred
                df[col].fillna(pd.Timestamp('2000-01-01'), inplace=True)
                df[col] = df[col].dt.strftime('%Y-%m-%d')  # Set to Tableau-friendly format
            except Exception:
                continue  # Skip if parsing fails
    
    return df


# Function to fill null values with random values
def fill_missing_values(df):
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == 'object':
                # Fill string columns with random choice from non-null values
                unique_values = df[col].dropna().unique()
                if len(unique_values) > 0:
                    df[col] = df[col].apply(lambda x: random.choice(unique_values) if pd.isnull(x) else x)
                else:
                    df[col].fillna('Unknown', inplace=True)
            elif df[col].dtype in ['int64', 'float64']:
                # Fill numeric columns with random integers within range
                if df[col].min() == df[col].max():
                    df[col].fillna(df[col].min(), inplace=True)
                else:
                    df[col].fillna(np.random.randint(df[col].min(), df[col].max() + 1), inplace=True)
            elif pd.api.types.is_datetime64_any_dtype(df[col]):
                # Fill date columns with a random date
                random_date = pd.to_datetime('2020-01-01') + pd.to_timedelta(np.random.randint(0, 365), unit='D')
                df[col].fillna(random_date.strftime('%Y-%m-%d'), inplace=True)
    return df


# Main function to process all datasets
def preprocess_data(file_list, output_path):
    # Get unified data types
    column_types = unify_data_types(file_list)
    
    for file in file_list:
        df = pd.read_csv(file)
        if df.empty:
            print(f"Skipping empty file: {file}")
            continue
        
        # Enforce consistent column data types
        for col in df.columns:
            if col in column_types:
                try:
                    df[col] = df[col].astype(column_types[col])
                except Exception as e:
                    print(f"Error converting column '{col}' in {file}: {e}")
        
        # Fill missing values
        df = fill_missing_values(df)
        
        # Format date columns
        df = format_date_columns(df)
        
        # Save the cleaned file to output path
        output_file = f"{output_path}/{os.path.basename(file).replace('.csv', '_cleaned.csv')}"
        df.to_csv(output_file, index=False)
        print(f"✅ Processed: {output_file}")


# Define path to all Blinkit CSV files
file_list = glob.glob('/Users/preshika/Downloads/archive/*.csv')
output_path = "/Users/preshika/Downloads/archive/cleaned"

# Ensure the output directory exists
os.makedirs(output_path, exist_ok=True)

# Run the preprocessing pipeline
preprocess_data(file_list, output_path)

print("All files processed successfully!")
