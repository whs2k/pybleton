# Python SDK Guide 🐍

The Pybleton Python SDK provides an asynchronous, strictly-typed wrapper around Ableton's Live Object Model (LOM).

## 💡 Quick Example

```python
import asyncio
from pybleton import Pybleton

async def main():
    # Connect via OSC to Ableton Live
    live = await Pybleton.connect(host="127.0.0.1", send_port=11000, recv_port=11001)

    # Access LiveSet properties
    print(f"Current Tempo: {live.set.tempo} BPM")

    # Traverse Tracks and Devices
    vocal_track = live.set.tracks["Vocal Lead"]
    reverb_device = vocal_track.devices["Reverb"]

    # Set parameter values asynchronously
    decay_param = reverb_device.parameters["Decay"]
    await decay_param.set_value(2.5)

    # Fire a clip
    await vocal_track.clips[0].fire()

    await live.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
```

## 🏗️ LOM Class Hierarchy

- **`Pybleton`**: Top-level SDK client entry point.
- **`LiveSet`**: Manages song-level parameters (tempo, signature, tracks).
- **`Track`**: Represents individual Audio, MIDI, or Return tracks.
- **`Device`**: Audio FX, MIDI FX, or Instruments loaded on a track.
- **`Parameter`**: Individual controllable device parameters with min/max validation.
- **`Clip`**: Audio or MIDI clips inside clip slots.
