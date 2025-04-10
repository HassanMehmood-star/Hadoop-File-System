#!/usr/bin/env python3
import sys

def reducer():
    current_feature = None
    total_completion = 0
    count = 0

    for line in sys.stdin:
        print(f"Received line: {line.strip()}")  # Debug print statement
        feature, completion_percentage = line.strip().split("\t")
        
        try:
            completion_percentage = float(completion_percentage)
        except ValueError:
            continue  # Skip lines where the value cannot be converted to float
        
        if current_feature == feature:
            total_completion += completion_percentage
            count += 1
        else:
            if current_feature:
                print(f"{current_feature}\t{total_completion / count}")  # Debug output
            current_feature = feature
            total_completion = completion_percentage
            count = 1

    if current_feature == feature:
        print(f"{current_feature}\t{total_completion / count}")  # Debug output

if __name__ == "__main__":
    reducer()
