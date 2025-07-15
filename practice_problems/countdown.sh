#!/bin/bash

count=5

while [ $count -ge 1 ]; do
  echo "$count..."
  sleep 1
  ((count--))
done

echo "🚀 branch_1 ready to Lift off!"

