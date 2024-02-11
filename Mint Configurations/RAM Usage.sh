#!/bin/bash

# Get used and total memory in bytes from free command
mem_info=$(free -b | grep "Mem:")
used_mem=$(echo $mem_info | awk '{print $3}')
total_mem=$(echo $mem_info | awk '{print $2}')

# Calculate RAM usage percentage and round up to nearest integer
ram_usage=$(echo "scale=0; ($used_mem * 100) / $total_mem" | bc)

echo "RAM: ${ram_usage}%"

