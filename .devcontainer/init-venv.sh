#!/bin/bash

# Check if the environment is already synced (by checking the presence of .uv.lock)
if [ ! -f ".uv.lock" ]; then
    echo "Syncing environment..."
    uv sync --frozen
else
    echo "Environment already synced."
fi

# Ensure virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv
fi
