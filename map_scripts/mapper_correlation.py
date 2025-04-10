#!/usr/bin/env python3
import sys

def mapper():
    for line in sys.stdin:
        # Split the input line into fields based on tab
        fields = line.strip().split("\t")
        
        # Check if the line has sufficient fields
        if len(fields) > 4:  # Ensuring there are at least 5 columns
            user_id = fields[0]          # User ID
            age = fields[1]              # Age
            gender = fields[2]           # Gender
            region = fields[3]           # Region
            completion_percentage = fields[4]  # Completion percentage
            
            # Emit key-value pairs for each feature and completion_percentage
            print(f"age\t{completion_percentage}")
            print(f"gender\t{completion_percentage}")
            print(f"region\t{completion_percentage}")

if __name__ == "__main__":
    mapper()
