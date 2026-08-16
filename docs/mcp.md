# FastMCP Agent Integration ⚡️

Pybleton features a zero-config Model Context Protocol (MCP) server powered by `FastMCP`.

## 🤖 Supported AI Clients

- **Claude Desktop** (macOS & Windows)
- **Cursor IDE**
- **Windsurf**
- **Custom MCP Client Applications**

## ⚡️ Zero-Config Auto Setup

Run this single command in your terminal:

```bash
pybleton configure-claude
```

This automatically modifies your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "pybleton": {
      "command": "uvx",
      "args": ["pybleton", "mcp"]
    }
  }
}
```

## 🧰 Available MCP Tools

| MCP Tool Name | Description | Arguments |
| :--- | :--- | :--- |
| `get_session_summary` | Introspects Ableton session (tracks, devices, tempo, clip status) | None |
| `set_tempo` | Sets the DAW master tempo (BPM) | `tempo: float` |
| `create_midi_track` | Adds a new MIDI track to the Live Set | `name: str` |
| `set_parameter_value` | Modifies any device parameter value in real-time | `track: str`, `device: str`, `parameter: str`, `value: float` |
| `fire_clip` | Triggers a clip in a specific track and slot | `track_index: int`, `clip_index: int` |
