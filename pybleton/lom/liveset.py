from typing import Dict, List
from pydantic import BaseModel, ConfigDict
from .track import Track, TrackModel
from pybleton.transport import Transport

class LiveSetModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    tempo: float
    tracks: List[TrackModel]

class LiveSet:
    """Represents the Ableton Live Set."""
    def __init__(self, transport: Transport, model: LiveSetModel):
        self.transport = transport
        self._model = model
        
        # Build tracks map
        self.tracks: Dict[str, Track] = {}
        for i, track_model in enumerate(model.tracks):
            track = Track(transport, i, track_model)
            self.tracks[track.name] = track

    @property
    def tempo(self) -> float:
        return self._model.tempo
        
    async def set_tempo(self, tempo: float):
        """Set the tempo of the Live Set."""
        address = "/live/song/set/tempo"
        await self.transport.send(address, tempo)
        self._model.tempo = tempo
