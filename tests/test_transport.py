import asyncio
import pytest
from pybleton.transport.osc import OSCTransport
from .mock_server import MockAbletonServer

@pytest.fixture
async def mock_server():
    server = MockAbletonServer()
    await server.start()
    yield server
    await server.stop()

@pytest.fixture
async def transport():
    trans = OSCTransport()
    await trans.connect()
    yield trans
    await trans.disconnect()

@pytest.mark.asyncio
async def test_osc_transport_send_receive(mock_server, transport):
    # Setup a Future to wait for the response
    loop = asyncio.get_running_loop()
    response_future = loop.create_future()
    
    async def handle_response(address, *args):
        response_future.set_result((address, args))
        
    # Register handler on transport
    transport.add_handler("/live/test/response", handle_response)
    
    # Send message to mock server
    await transport.send("/live/test", "hello", 123)
    
    # Wait for response with timeout
    address, args = await asyncio.wait_for(response_future, timeout=1.0)
    
    assert address == "/live/test/response"
    assert args == ("hello", 123)
    
    # Check mock server received the request
    assert mock_server.last_received == ("/live/test", ("hello", 123))
