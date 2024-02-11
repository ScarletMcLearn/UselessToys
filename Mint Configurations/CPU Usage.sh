#!/bin/bash

# Get CPU usage percentage and round up to nearest integer
cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{printf("%.0f\n", 100 - $1)}')

echo "CPU: ${cpu_usage}%"

