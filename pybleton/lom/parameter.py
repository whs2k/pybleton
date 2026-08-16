from pydantic import BaseModel, ConfigDict
from typing import Optional
from pybleton.transport import Transport

class ParameterModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    value: float
    min: float
    max: float
    is_quantized: bool

class Parameter:
    """Represents an Ableton Live Device Parameter."""
    def __init__(self, transport: Transport, track_idx: int, device_idx: int, param_idx: int, model: ParameterModel):
        self.transport = transport
        self.track_idx = track_idx
        self.device_idx = device_idx
        self.param_idx = param_idx
        self._model = model

    @property
    def name(self) -> str:
        return self._model.name
        
    @property
    def value(self) -> float:
        return self._model.value
        
    async def set_value(self, value: float):
        """Set the parameter's value asynchronously."""
        # For AbletonOSC the path is typically something like /live/track/device/param/set
        address = "/live/device/param/set/value"
        await self.transport.send(address, self.track_idx, self.device_idx, self.param_idx, value)
        self._model.value = value

