from typing import Dict, List
from pydantic import BaseModel, ConfigDict
from .parameter import Parameter, ParameterModel
from pybleton.transport import Transport

class DeviceModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    class_name: str
    parameters: List[ParameterModel]

class Device:
    """Represents an Ableton Live Device."""
    def __init__(self, transport: Transport, track_idx: int, device_idx: int, model: DeviceModel):
        self.transport = transport
        self.track_idx = track_idx
        self.device_idx = device_idx
        self._model = model
        
        # Build parameter map
        self.parameters: Dict[str, Parameter] = {}
        for i, param_model in enumerate(model.parameters):
            param = Parameter(transport, track_idx, device_idx, i, param_model)
            self.parameters[param.name] = param

    @property
    def name(self) -> str:
        return self._model.name

    @property
    def class_name(self) -> str:
        return self._model.class_name
