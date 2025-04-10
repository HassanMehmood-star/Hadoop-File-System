#!/usr/bin/env python3
import sys
import pandas as pd
from collections import defaultdict

def mapper():
    """Mapper function to read and process input data and split multi-label columns."""
    for line in sys.stdin:
        parts = line.strip().split("\t")
        
        # Skip lines with missing or incomplete data
        if len(parts) < 2:
            continue
        
        try:
            user_id = parts[0]  # Assuming user_id is in the first column
            hobbies = parts[1].split(",")  # Assuming hobbies is in the second column
            languages = parts[2].split(",")  # Assuming languages is in the third column

            # Emit a key-value pair for each hobby and language
            for hobby in hobbies:
                print(f"hobby:{hobby.strip()}\t1")
            for language in languages:
                print(f"language:{language.strip()}\t1")
        
        except ValueError:
            continue  # Skip invalid data

def reducer():
    """Reducer function to count the occurrences of each label (hobby or language)."""
    counts = defaultdict(int)
    
    # Aggregate the counts for each hobby and language
    for line in sys.stdin:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            label, count = parts
            counts[label] += int(count)
    
    # Output the counts for each hobby and language
    for label, count in counts.items():
        print(f"{label}\t{count}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mapper":
        mapper()
    elif len(sys.argv) > 1 and sys.argv[1] == "reducer":
        reducer()