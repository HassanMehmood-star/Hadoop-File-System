#!/usr/bin/env python3
import sys
from datetime import datetime

def mapper():
    """Mapper function to calculate days_since_registration."""
    for line in sys.stdin:
        parts = line.strip().split("\t")
        
        # Skip lines with missing data
        if len(parts) < 2:
            continue

        try:
            user_id = parts[0]
            registration_date = parts[1]
            last_login_date = parts[2]

            # Convert to datetime objects
            registration_datetime = datetime.strptime(registration_date, "%Y-%m-%d")
            last_login_datetime = datetime.strptime(last_login_date, "%Y-%m-%d")
            
            # Calculate days since registration
            days_since_registration = (last_login_datetime - registration_datetime).days
            
            # Output the user_id and days since registration
            print(f"{user_id}\t{days_since_registration}")
        
        except ValueError:
            continue  # Skip lines with invalid data

def reducer():
    """Reducer function to collect and output days_since_registration."""
    # Since we just pass through the data from mapper, we do not need to aggregate or process
    # anything further in the reducer in this case.
    for line in sys.stdin:
        # Simply print the data passed from mapper
        print(line.strip())

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "mapper":
        mapper()
    elif len(sys.argv) > 1 and sys.argv[1] == "reducer":
        reducer()