#!/bin/bash

# Sync changes
git pull

# Define the file name and path
counter_file="counter.txt"

# Check if the counter file exists, if not, create it and initialise the counter to 0
if [ ! -f "$counter_file" ]; then
	echo "0" > "$counter_file"
fi

# Read the current value of the counter from the file
counter=$(<counter.txt) 

# Increment the counter
((counter++))

# Update the counter in the file
echo "$counter" > "$counter_file"

# Display the updated counter value
echo "Counter incremented. New value: $counter"

# Stage and commit changes to Git
git add "$counter_file"
git commit -m "Counter incremented. New value: $counter"
git push
