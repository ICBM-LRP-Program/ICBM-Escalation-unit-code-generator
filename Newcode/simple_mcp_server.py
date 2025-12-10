#!/usr/bin/env python3
"""
Simple MCP server for testing
"""
import sys
import json

def main():
    # Read initialization message
    line = sys.stdin.readline()
    if not line:
        return
    
    try:
        data = json.loads(line)
        # Send initialization response
        response = {
            "jsonrpc": "2.0",
            "id": data.get("id"),
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "serverInfo": {
                    "name": "test-mcp",
                    "version": "1.0.0"
                }
            }
        }
        print(json.dumps(response), flush=True)
        
        # Keep connection open
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            try:
                msg = json.loads(line)
                # Echo back
                echo = {
                    "jsonrpc": "2.0",
                    "id": msg.get("id"),
                    "result": {"echo": "received"}
                }
                print(json.dumps(echo), flush=True)
            except:
                pass
                
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
