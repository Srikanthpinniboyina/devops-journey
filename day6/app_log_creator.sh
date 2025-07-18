#!/bin/bash
read -p "enter the folder name" folder
mkdir -p "$folder"
log_file="$folder/app.log"
current_time=$(date '+%Y-%m-%d %H:%M:%S')
echo "Current time: $current_time" > "$log_file"
echo "log created" >> "$log_file"
echo "log file createa at $log_file"

