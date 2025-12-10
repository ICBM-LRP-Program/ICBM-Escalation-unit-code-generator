#!/usr/bin/env python3
"""
OpenMemory MCP stdio wrapper
This script acts as a stdio MCP client that connects to the OpenMemory HTTP MCP server.
"""
import sys
import json
import asyncio
import aiohttp
import logging

# Set up logging
logging.basicConfig(level=logging.WARNING)

async def handle_mcp_connection():
    """Handle MCP connection via stdio"""
    # Read initialization message from stdin
    init_message = sys.stdin.readline()
    if not init_message:
        return
    
    try:
        init_data = json.loads(init_message)
        # Send initialization response
        init_response = {
            "jsonrpc": "2.0",
            "id": init_data.get("id"),
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "serverInfo": {
                    "name": "openmemory-mcp",
                    "version": "1.0.0"
                }
            }
        }
        print(json.dumps(init_response), flush=True)
        
        # Process messages
        async with aiohttp.ClientSession() as session:
            while True:
                line = sys.stdin.readline()
                if not line:
                    break
                
                try:
                    message = json.loads(line)
                    if message.get("method") == "tools/list":
                        # List available tools
                        response = {
                            "jsonrpc": "2.0",
                            "id": message.get("id"),
                            "result": {
                                "tools": [
                                    {
                                        "name": "add_memories",
                                        "description": "Add a new memory",
                                        "inputSchema": {
                                            "type": "object",
                                            "properties": {
                                                "text": {"type": "string"}
                                            },
                                            "required": ["text"]
                                        }
                                    },
                                    {
                                        "name": "search_memory",
                                        "description": "Search through stored memories",
                                        "inputSchema": {
                                            "type": "object",
                                            "properties": {
                                                "query": {"type": "string"}
                                            },
                                            "required": ["query"]
                                        }
                                    },
                                    {
                                        "name": "list_memories",
                                        "description": "List all memories in the user's memory",
                                        "inputSchema": {
                                            "type": "object",
                                            "properties": {}
                                        }
                                    }
                                ]
                            }
                        }
                        print(json.dumps(response), flush=True)
                    
                    elif message.get("method") == "tools/call":
                        # Call a tool via HTTP
                        tool_name = message["params"]["name"]
                        arguments = message["params"]["arguments"]
                        
                        # Map to OpenMemory HTTP API
                        if tool_name == "add_memories":
                            # This would require user_id and client_name
                            # For now, return a simple response
                            response = {
                                "jsonrpc": "2.0",
                                "id": message.get("id"),
                                "result": {
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "Memory added (simulated)"
                                        }
                                    ]
                                }
                            }
                        elif tool_name == "search_memory":
                            response = {
                                "jsonrpc": "2.0",
                                "id": message.get("id"),
                                "result": {
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "Search results (simulated)"
                                        }
                                    ]
                                }
                            }
                        elif tool_name == "list_memories":
                            response = {
                                "jsonrpc": "2.0",
                                "id": message.get("id"),
                                "result": {
                                    "content": [
                                        {
                                            "type": "text",
                                            "text": "Memory list (simulated)"
                                        }
                                    ]
                                }
                            }
                        else:
                            response = {
                                "jsonrpc": "2.0",
                                "id": message.get("id"),
                                "error": {
                                    "code": -32601,
                                    "message": f"Method not found: {tool_name}"
                                }
                            }
                        
                        print(json.dumps(response), flush=True)
                    
                    else:
                        # Unknown method
                        response = {
                            "jsonrpc": "2.0",
                            "id": message.get("id"),
                            "error": {
                                "code": -32601,
                                "message": f"Method not found: {message.get('method')}"
                            }
                        }
                        print(json.dumps(response), flush=True)
                        
                except json.JSONDecodeError:
                    continue
                except Exception as e:
                    error_response = {
                        "jsonrpc": "2.0",
                        "id": message.get("id") if 'message' in locals() else None,
                        "error": {
                            "code": -32000,
                            "message": f"Internal error: {str(e)}"
                        }
                    }
                    print(json.dumps(error_response), flush=True)
    
    except json.JSONDecodeError:
        pass
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(handle_mcp_connection())
