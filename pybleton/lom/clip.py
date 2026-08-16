from pydantic import BaseModel, ConfigDict
from typing import Optional
from pybleton.transport import Transport

class ClipModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    length: float
    is_midi: bool

class Clip:
    """Represents an Ableton Live Clip."""
    def __init__(self, transport: Transport, track_idx: int, clip_idx: int, model: ClipModel):
        self.transport = transport
        self.track_idx = track_idx
        self.clip_idx = clip_idx
        self._model = model

    @property
    def name(self) -> str:
        return self._model.name

    async def fire(self):
        """Trigger this clip."""
        address = "/live/clip/fire"
        await self.transport.send(address, self.track_idx, self.clip_idx)

