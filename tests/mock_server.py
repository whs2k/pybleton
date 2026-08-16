import asyncio
import logging
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient

logger = logging.getLogger(__name__)

class MockAbletonServer:
    """Mock Ableton OSC Server for testing."""
    
    def __init__(self, host: str = "127.0.0.1", listen_port: int = 11000, send_port: int = 11001):
        self.host = host
        self.listen_port = listen_port
        self.send_port = send_port
        
        self.dispatcher = Dispatcher()
        self.dispatcher.set_default_handler(self._default_handler)
        self.dispatcher.map("/live/test", self._handle_test)
        
        self.client = SimpleUDPClient(self.host, self.send_port)
        self.server = None
        self.transport = None
        
        self.last_received = None

    async def start(self):
        loop = asyncio.get_running_loop()
        self.server = AsyncIOOSCUDPServer((self.host, self.listen_port), self.dispatcher, loop)
        self.transport, _ = await self.server.create_serve_endpoint()
        
    async def stop(self):
        if self.transport:
            self.transport.close()

    def _default_handler(self, address: str, *args):
        self.last_received = (address, args)
        logger.debug(f"Mock server received: {address} {args}")
        
    def _handle_test(self, address: str, *args):
        self.last_received = (address, args)
        # Echo back a response to testing endpoint
        self.client.send_message("/live/test/response", args)

