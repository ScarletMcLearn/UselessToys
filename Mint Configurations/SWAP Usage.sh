#!/bin/bash

# Get swap usage percentage and round up to nearest integer
swap_usage=$(free | awk '/Swap/ {printf("%.0f\n", ($3/$2)*100)}')

echo "SWAP: ${swap_usage}%"

