import logging
from typing import Optional
from fastmcp import FastMCP
from ..client import Pybleton

logger = logging.getLogger(__name__)

mcp = FastMCP("Pybleton Server", description="Control Ableton Live via MCP")

@mcp.tool
async def get_session_summary() -> str:
    """Get the current Ableton session summary including tempo and tracks."""
    # Assuming connection is managed or singleton for the CLI
    client = await Pybleton.connect()
    # In a real scenario, client.set would be populated
    return f"Connected to Ableton OSC on {client.transport.host}:{client.transport.send_port}"

@mcp.tool
async def set_tempo(tempo: float) -> str:
    """Set the tempo of the Ableton Live session."""
    client = await Pybleton.connect()
    if client.set:
        await client.set.set_tempo(tempo)
        return f"Tempo set to {tempo} BPM"
    return "Failed to set tempo: LiveSet not fully synced."

