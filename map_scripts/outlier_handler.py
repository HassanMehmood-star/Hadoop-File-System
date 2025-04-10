#!/usr/bin/env python3
import sys
import numpy as np

def mapper():
    """Mapper function to process input data and extract relevant features."""
    for line in sys.stdin:
        parts = line.strip().split("\t")
        if len(parts) < 2:
            continue
        try:
            # Assume the first column is age and the second column is completion percentage
            age = float(parts[0])
            completion_percentage = float(parts[1])
            print(f"{age}\t{completion_percentage}")
        except ValueError:
            continue  # Skip invalid lines

def reducer():
    """Reducer function to calculate quartiles and identify outliers."""
    data = []

    # Collect all input data
    for line in sys.stdin:
        try:
            age, completion_percentage = map(float, line.strip().split("\t"))
            data.append(completion_percentage)  # Using completion_percentage to identify outliers
        except ValueError:
            continue  # Skip invalid data

    if not data:
        return

    # Convert to numpy array for statistical analysis
    data = np.array(data)
    
    # Calculate Q1, Q3, and IQR
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1

    # Define outlier thresholds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Filter outliers
    filtered_data = [x for x in data if lower_bound <= x <= upper_bound]

    # Print statistics for filtered data
    print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
    print(f"Outlier removal resulted in {len(data) - len(filtered_data)} outliers removed.")
    print(f"Filtered data: {filtered_data[:10]}")  # Print first 10 valid entries for review

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mapper":
        mapper()
    elif len(sys.argv) > 1 and sys.argv[1] == "reducer":
        reducer()
