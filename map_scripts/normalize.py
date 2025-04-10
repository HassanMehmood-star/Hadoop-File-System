#!/usr/bin/env python3
import sys
import numpy as np

def mapper():
    """Mapper function to process age and output it for normalization."""
    for line in sys.stdin:
        parts = line.strip().split("\t")
        
        if len(parts) < 2:
            continue
        
        try:
            user_id = parts[0]  # Assuming user_id is in the first column
            age = float(parts[1])  # Assuming age is in the second column

            # Emit the age for normalization
            print(f"{user_id}\t{age}")
        
        except ValueError:
            continue  # Skip lines with invalid data

def reducer():
    """Reducer function to calculate mean, standard deviation and normalize age."""
    ages = []

    # Collect all the ages
    for line in sys.stdin:
        try:
            user_id, age = line.strip().split("\t")
            age = float(age)
            ages.append(age)
        except ValueError:
            continue  # Skip invalid data

    if not ages:
        return

    # Convert to numpy array for statistical calculations
    ages = np.array(ages)

    # Calculate mean and standard deviation
    mean_age = np.mean(ages)
    std_age = np.std(ages)

    # Output the mean and standard deviation
    print(f"mean:{mean_age}\tstd:{std_age}")

    # Normalize (Z-Score) and print results
    for age in ages:
        normalized_age = (age - mean_age) / std_age
        print(f"{normalized_age}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mapper":
        mapper()
    elif len(sys.argv) > 1 and sys.argv[1] == "reducer":
        reducer()