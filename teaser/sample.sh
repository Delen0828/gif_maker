#!/bin/bash

# Define the source directory and output directory
source_dir="dirs"
output_dir="out"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Iterate through each subdirectory in the source directory
for dir in "$source_dir"/*; do
    if [ -d "$dir" ]; then  # Check if it's a directory
        # Copy the specified files to the output directory
        cp "$dir/ezgif-frame-006.png" "$output_dir/$dir-006.png"
        cp "$dir/ezgif-frame-009.png" "$output_dir/$dir-009.png"
        cp "$dir/ezgif-frame-012.png" "$output_dir/$dir-012.png"
        cp "$dir/ezgif-frame-015.png" "$output_dir/$dir-015.png"
        cp "$dir/ezgif-frame-018.png" "$output_dir/$dir-018.png"
        cp "$dir/ezgif-frame-021.png" "$output_dir/$dir-021.png"
    fi
done

echo "Files copied to $output_dir"
