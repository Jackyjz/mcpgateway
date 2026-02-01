from fastmcp import FastMCP
import platform

mcp = FastMCP("gateway-mcp")

@mcp.tool()
def echo(text: str) -> str:
    """Echo back the input text"""
    return text

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def identity() ->str:
    """Return basic identity of this server """
    return (
        "I am gateway-mcp: a dummy MCP server running inside the API layer prototype. "
        f"Platform={platform.system()}."
    )

if __name__ == "__main__":
    mcp.run()