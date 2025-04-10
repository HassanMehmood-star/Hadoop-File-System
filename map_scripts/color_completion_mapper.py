#!/usr/bin/env python

import sys

# Mapper function
def mapper():
    for line in sys.stdin:
        # Strip leading/trailing whitespaces
        line = line.strip()
        
        # Split the line into fields (assuming tab-separated format)
        fields = line.split("\t")
        
        # Check if the line has the correct number of columns
        if len(fields) >= 2:
            # Extract 'favourite_color' and 'completion_percentage' from the line
            favourite_color = fields[1]  # Adjust based on actual column (column 1 for favourite_color)
            try:
                completion_percentage = float(fields[2])  # Adjust based on actual column (column 2 for completion_percentage)
                
                # Emit key-value pair
                print(f"{favourite_color}\t{completion_percentage}")
            except ValueError:
                # In case 'completion_percentage' is missing or invalid, skip the line
                continue

# Run the mapper function
if __name__ == "__main__":
    mapper()