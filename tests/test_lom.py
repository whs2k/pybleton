import pytest
import asyncio
from pybleton.client import Pybleton
from pybleton.lom.liveset import LiveSetModel
from pybleton.lom.track import TrackModel
from pybleton.lom.device import DeviceModel
from pybleton.lom.parameter import ParameterModel
from pybleton.lom.clip import ClipModel

from .mock_server import MockAbletonServer

@pytest.fixture
def mock_liveset_model():
    return LiveSetModel(
        tempo=120.0,
        tracks=[
            TrackModel(
                name="Vocal Lead",
                color=1,
                is_foldable=False,
                devices=[
                    DeviceModel(
                        name="Reverb",
                        class_name="Reverb",
                        parameters=[
                            ParameterModel(name="Decay", value=1.0, min=0.0, max=10.0, is_quantized=False),
                            ParameterModel(name="Dry/Wet", value=0.5, min=0.0, max=1.0, is_quantized=False)
                        ]
                    )
                ],
                clips=[
                    ClipModel(name="Intro", length=4.0, is_midi=False),
                    None
                ]
            )
        ]
    )

@pytest.fixture
async def mock_server():
    server = MockAbletonServer()
    await server.start()
    yield server
    await server.stop()

@pytest.fixture
async def pybleton_client():
    client = await Pybleton.connect()
    yield client
    await client.disconnect()

@pytest.mark.asyncio
async def test_lom_structure_and_set_parameter(mock_server, pybleton_client, mock_liveset_model):
    # Setup state
    from pybleton.lom.liveset import LiveSet
    pybleton_client.set = LiveSet(pybleton_client.transport, mock_liveset_model)
    
    # Traverse hierarchy
    track = pybleton_client.set.tracks["Vocal Lead"]
    assert track.name == "Vocal Lead"
    
    reverb = track.devices["Reverb"]
    assert reverb.class_name == "Reverb"
    
    decay_param = reverb.parameters["Decay"]
    assert decay_param.value == 1.0
    
    # Test setting a parameter
    await decay_param.set_value(2.5)
    
    # Let async event loop run to send OSC message
    await asyncio.sleep(0.01)
    
    # Check mock server received the correct OSC message
    address, args = mock_server.last_received
    assert address == "/live/device/param/set/value"
    
    # The message should be (track_idx, device_idx, param_idx, value)
    assert args == (0, 0, 0, 2.5)
    
    # Verify local state was updated
    assert decay_param.value == 2.5

@pytest.mark.asyncio
async def test_fire_clip(mock_server, pybleton_client, mock_liveset_model):
    from pybleton.lom.liveset import LiveSet
    pybleton_client.set = LiveSet(pybleton_client.transport, mock_liveset_model)
    
    clip = pybleton_client.set.tracks["Vocal Lead"].clips[0]
    await clip.fire()
    
    await asyncio.sleep(0.01)
    
    address, args = mock_server.last_received
    assert address == "/live/clip/fire"
    assert args == (0, 0)
