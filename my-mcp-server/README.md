# MCP Server Examples

This directory contains examples of MCP (Model Context Protocol) servers that extend Claude's capabilities.

## Available Servers

### 1. File Server (`file_server.py`)
- **Purpose**: File operations (list, read, write, get info)
- **Tools**:
  - `list_files`: List files in a directory
  - `read_file`: Read file contents
  - `write_file`: Write content to a file
  - `get_file_info`: Get file/directory metadata

### 2. Weather Server (`weather_server.py`)
- **Purpose**: Weather data from external API
- **Tools**:
  - `get_weather`: Get current weather for a city
  - `get_weather_forecast`: Get weather forecast

## Setup Instructions

### 1. Install Dependencies
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install MCP SDK
pip install mcp
```

### 2. Configure Claude
Add this to your `~/.claude/mcp.json`:

```json
{
  "mcpServers": {
    "file-server": {
      "command": "python3",
      "args": ["/full/path/to/my-mcp-server/file_server.py"]
    },
    "weather-server": {
      "command": "python3",
      "args": ["/full/path/to/my-mcp-server/weather_server.py"]
    }
  }
}
```

**Note**: Update the full paths to match your actual file locations.

### 3. Test the Servers

#### Test File Server
```bash
# Test tool listing
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | python3 file_server.py

# Test file operation
echo '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"list_files"}}' | python3 file_server.py
```

#### Test Weather Server
```bash
# Note: Requires API key from weatherapi.com
# Update the API key in weather_server.py first
```

## Best Practices

1. **Security**: Never expose sensitive operations without proper authentication
2. **Input Validation**: Always validate and sanitize inputs
3. **Error Handling**: Return meaningful error messages
4. **Async Operations**: Use async/await for I/O operations
5. **Idempotency**: Tools should be safe to retry

## Running the Servers

Start the server with:
```bash
python3 file_server.py
# or
python3 weather_server.py
```

The server will run via stdio transport, which is what Claude expects.

## Troubleshooting

1. **Module not found**: Ensure you've installed `mcp` package
2. **Path issues**: Verify absolute paths in mcp_config.json
3. **Permissions**: Ensure Claude has permission to execute the Python files
4. **API keys**: Update placeholder API keys with real ones

## Advanced Examples

Check the comments in the source files for:
- Database integration examples
- External API patterns  
- Resource definitions (read-only data)
- File system operations