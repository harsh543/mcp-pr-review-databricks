from fastmcp import FastMCP

mcp = FastMCP("hello_mcp")

@mcp.on_initialize
async def handle_initialize(params):
    return {"capabilities": {}}

if __name__ == "__main__":
    mcp.run(transport="stdio")
