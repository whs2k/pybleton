<div align="center">
  <h1>Pybleton</h1>
  <p><b>The modern, asynchronous Python SDK & FastMCP Server for Ableton Live.</b></p>
  <p>Control Ableton with Python, Claude Desktop, Cursor, and Windsurf in seconds.</p>
</div>

---

## ⚡️ Zero-Friction Setup

If you have Ableton Live installed, you can get Pybleton running and connected to Claude Desktop in **under 60 seconds**.

### 1. Install Pybleton
```bash
pip install pybleton
```

### 2. Auto-Install the Ableton Remote Script
Pybleton includes an auto-installer that injects our Remote Script into your Ableton `User Library`.
```bash
pybleton install
```
*(Open Ableton -> Preferences -> Link/Tempo/MIDI -> Select 'Pybleton' as a Control Surface)*

### 3. Connect to Claude Desktop (Magic 🪄)
Want Claude to generate beats for you? Run this command to inject our FastMCP server into your Claude configuration:
```bash
pybleton configure-claude
```
*(Restart Claude Desktop and you're done!)*

## 🐍 For Python Developers (The SDK)

Pybleton isn't just an MCP server. It is a strictly-typed, asynchronous, object-oriented LOM (Live Object Model) wrapper.

```python
import asyncio
from pybleton import Pybleton

async def main():
    # Connect asynchronously
    live = await Pybleton.connect()
    
    # Introspect your session with full IntelliSense
    track = live.set.tracks["Vocal Lead"]
    
    # Modify parameters asynchronously (no blocking!)
    await track.devices["Reverb"].parameters["Dry/Wet"].set_value(0.45)
    
    # Fire clips
    await track.clips[0].fire()

asyncio.run(main())
```

## 🤝 Community & Contributing
We want this to be the definitive open-source Python library for Ableton Live.
Check out our [Contributing Guidelines](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md). We welcome PRs for new LOM mappings!
