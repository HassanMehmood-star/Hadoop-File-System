#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def mapper():
    """Mapper function to read and process input data and output encoded categorical variables."""
    encoder = OneHotEncoder(sparse=False)  # Encoder to handle one-hot encoding
    
    for line in sys.stdin:
        parts = line.strip().split("\t")
        
        # Skip invalid lines
        if len(parts) < 4:
            continue
        
        try:
            gender = parts[0]  # Assuming gender is in the first column
            region = parts[1]  # Assuming region is in the second column
            eye_color = parts[2]  # Assuming eye_color is in the third column
            other_feature = parts[3]  # Another categorical variable (replace with real feature)

            # Encode categorical features using one-hot encoding
            encoded_gender = encoder.fit_transform([[gender]])[0]  # One-hot encoding gender
            encoded_region = encoder.fit_transform([[region]])[0]  # One-hot encoding region
            encoded_eye_color = encoder.fit_transform([[eye_color]])[0]  # One-hot encoding eye_color

            # Output the encoded features as a tab-separated line
            output = f"{gender}\t{region}\t{eye_color}\t" \
                     f"{','.join(map(str, encoded_gender))}\t" \
                     f"{','.join(map(str, encoded_region))}\t" \
                     f"{','.join(map(str, encoded_eye_color))}"
            print(output)
        except ValueError:
            continue  # Skip invalid data

def reducer():
    """Reducer function to output the aggregated data after encoding."""
    data = []
    
    for line in sys.stdin:
        try:
            parts = line.strip().split("\t")
            
            # Assuming the input is the result of the mapper (including encoded data)
            gender = parts[0]
            region = parts[1]
            eye_color = parts[2]
            encoded_gender = parts[3].split(",")
            encoded_region = parts[4].split(",")
            encoded_eye_color = parts[5].split(",")
            
            # Convert the encoded values to numeric format for processing
            encoded_gender = list(map(float, encoded_gender))
            encoded_region = list(map(float, encoded_region))
            encoded_eye_color = list(map(float, encoded_eye_color))
            
            data.append([gender, region, eye_color] + encoded_gender + encoded_region + encoded_eye_color)
        except ValueError:
            continue  # Skip invalid data

    # You can perform some aggregation here if needed, or simply output the data
    # For now, just print the collected data (This is just an example)
    for item in data:
        print("\t".join(map(str, item)))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mapper":
        mapper()
    elif len(sys.argv) > 1 and sys.argv[1] == "reducer":
        reducer()
