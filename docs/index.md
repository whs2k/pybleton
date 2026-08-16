# Pybleton

**Pybleton** is a modern, asynchronous, strictly-typed Python SDK wrapping Ableton's Live Object Model (LOM), coupled with a first-class MCP server built with `FastMCP`.

## Target Audience

1. **Human Developers & Researchers:** Clean Pythonic APIs, async event loops, complete type safety, and clear documentation.
2. **AI Coding Agents:** Self-documenting class signatures with explicit PEP 484 Type Hints.
3. **End-Users & Prompt-Based Producers:** Instant, zero-friction integration with Claude Desktop and Cursor using standard MCP tool calling.

## Architecture

1. **Transport Layer:** Asynchronous networking (`asyncio`) utilizing OSC to communicate with Ableton Live.
2. **Object Model Layer:** Mapping raw network payloads to typed Python abstractions (`LiveSet`, `Track`, `Device`, `Parameter`, `Clip`).
3. **FastMCP Server Layer:** Exposing the SDK's capabilities directly to AI desktop clients via standard MCP tools.
4. **Type-Safety:** Enforced by Pydantic V2 schemas for message serialization and tool argument parsing.

## Quick Start

```python
import asyncio
from pybleton import Pybleton

async def main():
    # Connect to the local Ableton OSC remote script
    live = await Pybleton.connect(host="127.0.0.1", port=11000)
    
    # Introspect the session state
    print(live.set.tempo)
    
    # Access a track and modify a parameter asynchronously
    track = live.set.tracks["Vocal Lead"]
    await track.devices["Reverb"].parameters["Dry/Wet"].set_value(0.45)
    
    # Fire a clip
    await track.clips[0].fire()

asyncio.run(main())
```

To run the MCP server:
```bash
uvx pybleton mcp
```
