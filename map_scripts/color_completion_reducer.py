#!/usr/bin/env python

import sys
import numpy as np

# Reducer function
def reducer():
    current_color = None
    values = []

    for line in sys.stdin:
        # Strip leading/trailing whitespaces
        line = line.strip()

        # Parse the key-value pair
        favourite_color, completion_percentage = line.split("\t")

        # Convert the completion percentage to a float
        try:
            completion_percentage = float(completion_percentage)
        except ValueError:
            continue  # Skip invalid entries

        # If we're still processing the same color, accumulate the values
        if favourite_color == current_color:
            values.append(completion_percentage)
        else:
            if current_color:
                # Process the previous color and output statistics
                mean = np.mean(values)
                median = np.median(values)
                print(f"{current_color}\t{mean:.2f}\t{median:.2f}")
            
            # Set the current color to the new one and reset the values list
            current_color = favourite_color
            values = [completion_percentage]
    
    # Output the statistics for the last color
    if current_color:
        mean = np.mean(values)
        median = np.median(values)
        print(f"{current_color}\t{mean:.2f}\t{median:.2f}")

# Run the reducer function
if __name__ == "__main__":
    reducer()