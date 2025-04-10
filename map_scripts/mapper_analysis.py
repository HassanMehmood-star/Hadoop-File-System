#!/usr/bin/env python3
import sys

# Mapper function
for line in sys.stdin:
    # Clean the input line and split by tabs
    fields = line.strip().split('\t')
    
    # Assuming the format is:
    # user_id\tage\tgender\tregion\tother_fields
    
    # Extracting AGE, Gender, and Region from the respective columns
    try:
        age = fields[1]  # Assuming the second column is age
        gender = fields[2]  # Assuming the third column is gender
        region = fields[3]  # Assuming the fourth column is region
        
        # Emit the key-value pairs for each of the features
        print(f'AGE:{age}\t1')
        print(f'Gender:{gender}\t1')
        print(f'Region:{region}\t1')
    
    except IndexError:
        # Handle missing values or malformed lines (skip them)
        continue
