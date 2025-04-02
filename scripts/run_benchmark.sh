#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/../src"

echo "CPU Information:"
lscpu
echo "----------------------------------------"
echo "Memory Information:"
free -h
echo "----------------------------------------"

make clean
make

cd "$SCRIPT_DIR/../analise"
python3 benchmark.py && \
    python3 plot.py
