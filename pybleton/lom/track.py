from typing import Dict, List, Optional
from pydantic import BaseModel, ConfigDict
from .device import Device, DeviceModel
from .clip import Clip, ClipModel
from pybleton.transport import Transport

class TrackModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    color: int
    is_foldable: bool
    devices: List[DeviceModel]
    clips: List[Optional[ClipModel]]

class Track:
    """Represents an Ableton Live Track."""
    def __init__(self, transport: Transport, track_idx: int, model: TrackModel):
        self.transport = transport
        self.track_idx = track_idx
        self._model = model
        
        # Build devices map
        self.devices: Dict[str, Device] = {}
        for i, device_model in enumerate(model.devices):
            device = Device(transport, track_idx, i, device_model)
            self.devices[device.name] = device
            
        # Build clips map
        self.clips: Dict[int, Clip] = {}
        for i, clip_model in enumerate(model.clips):
            if clip_model is not None:
                self.clips[i] = Clip(transport, track_idx, i, clip_model)

    @property
    def name(self) -> str:
        return self._model.name
