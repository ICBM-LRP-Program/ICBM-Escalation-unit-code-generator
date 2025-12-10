#!/usr/bin/env python3
"""
Script to start OpenMemory MCP server for stdio mode
"""
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Change to the api directory
api_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mem0", "openmemory", "api")
os.chdir(api_dir)

# Import and run uvicorn
import uvicorn
from main import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8765)
