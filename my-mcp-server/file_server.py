#!/usr/bin/env python3
"""file_server.py - MCP server for file operations"""

import os
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server

server = Server("file-server")

@server.tool()
async def list_files(directory: str = ".") -> str:
    """List files in a directory.
    
    Args:
        directory: Directory path to list (default: current directory)
    """
    try:
        if not os.path.exists(directory):
            return f"Error: Directory '{directory}' does not exist"
        
        if not os.path.isdir(directory):
            return f"Error: '{directory}' is not a directory"
        
        items = os.listdir(directory)
        files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
        dirs = [item for item in items if os.path.isdir(os.path.join(directory, item))]
        
        result = {
            "directory": directory,
            "files": files,
            "directories": dirs,
            "total_files": len(files),
            "total_directories": len(dirs)
        }
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error listing files: {str(e)}"

@server.tool()
async def read_file(path: str) -> str:
    """Read the contents of a file.
    
    Args:
        path: File path to read
    """
    try:
        if not os.path.exists(path):
            return f"Error: File '{path}' does not exist"
        
        if not os.path.isfile(path):
            return f"Error: '{path}' is not a file"
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"

@server.tool()
async def write_file(path: str, content: str) -> str:
    """Write content to a file.
    
    Args:
        path: File path to write
        content: Content to write to the file
    """
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return f"Successfully wrote to '{path}'"
    except Exception as e:
        return f"Error writing file: {str(e)}"

@server.tool()
async def get_file_info(path: str) -> str:
    """Get information about a file or directory.
    
    Args:
        path: Path to get information about
    """
    try:
        if not os.path.exists(path):
            return f"Error: Path '{path}' does not exist"
        
        stat = os.stat(path)
        info = {
            "path": path,
            "is_file": os.path.isfile(path),
            "is_directory": os.path.isdir(path),
            "size_bytes": stat.st_size,
            "modified_time": stat.st_mtime,
            "created_time": stat.st_ctime,
            "readable": os.access(path, os.R_OK),
            "writable": os.access(path, os.W_OK)
        }
        return json.dumps(info, indent=2)
    except Exception as e:
        return f"Error getting file info: {str(e)}"

# Run server
async def main():
    async with stdio_server() as (read, write):
        await server.run(read, write)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())