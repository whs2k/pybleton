# Pybleton Cookbook 🧑‍🍳

Welcome to the Pybleton Cookbook! Here are some killer use-cases to inspire you.

## 🤖 1. The "Claude Producer"
Once you've run `pybleton configure-claude` and selected Pybleton in Ableton's MIDI Preferences, open Claude Desktop and try these prompts:

* "Analyze my current Ableton session. What tempo am I at, and how many tracks do I have?"
* "Create a new MIDI track called 'Synth Bass' and load an Analog device onto it."
* "Set the tempo to 128 BPM and start playback."

Because Pybleton exposes Ableton's LOM via the **Model Context Protocol (MCP)**, Claude understands exactly what tools are available and how to use them!

## 🎛️ 2. Algorithmic Composition (Python)
Use `asyncio` to generate generative music without blocking the main event loop.

```python
import asyncio
import random
from pybleton import Pybleton

async def generative_macro_twister(device):
    """Randomly tweaks a macro knob every 1/4 note."""
    param = device.parameters["Macro 1"]
    while True:
        new_val = random.uniform(0.0, 1.0)
        await param.set_value(new_val)
        await asyncio.sleep(0.5)  # Wait 500ms
        
async def main():
    live = await Pybleton.connect()
    device = live.set.tracks[0].devices[0]
    
    # Run the generative task in the background
    asyncio.create_task(generative_macro_twister(device))
    
    # Keep the script running
    await asyncio.Future() 
```
