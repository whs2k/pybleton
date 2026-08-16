import asyncio
import logging
from typing import Callable, Any, Dict, List, Awaitable

from pythonosc.osc_message_builder import OscMessageBuilder
from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
from pythonosc.udp_client import SimpleUDPClient

from .base import Transport, HandlerFunc

logger = logging.getLogger(__name__)

class OSCTransport(Transport):
    """OSC Transport implementation using python-osc."""
    
    def __init__(self, host: str = "127.0.0.1", send_port: int = 11000, recv_port: int = 11001):
        self.host = host
        self.send_port = send_port
        self.recv_port = recv_port
        self.client = SimpleUDPClient(self.host, self.send_port)
        self.dispatcher = Dispatcher()
        self.dispatcher.set_default_handler(self._default_handler)
        self.server = None
        self.transport = None
        
        self.handlers: Dict[str, List[HandlerFunc]] = {}
        
    async def connect(self):
        """Connect the OSC server to receive messages."""
        logger.info(f"Connecting OSC Transport. Sending to {self.send_port}, Listening on {self.recv_port}")
        loop = asyncio.get_running_loop()
        self.server = AsyncIOOSCUDPServer((self.host, self.recv_port), self.dispatcher, loop)
        self.transport, _ = await self.server.create_serve_endpoint()
        
    async def disconnect(self):
        """Disconnect the OSC server."""
        if self.transport:
            self.transport.close()
            
    async def send(self, address: str, *args: Any):
        """Send an OSC message."""
        logger.debug(f"Sending OSC: {address} {args}")
        # Note: python-osc SimpleUDPClient is synchronous but non-blocking for UDP.
        self.client.send_message(address, args)
        
    def add_handler(self, address: str, handler: HandlerFunc):
        """Register a handler for an OSC address."""
        if address not in self.handlers:
            self.handlers[address] = []
            self.dispatcher.map(address, self._dispatch_osc)
        self.handlers[address].append(handler)
        
    def remove_handler(self, address: str, handler: HandlerFunc):
        """Remove a handler."""
        if address in self.handlers:
            self.handlers[address].remove(handler)
            if not self.handlers[address]:
                del self.handlers[address]
                self.dispatcher.unmap(address, self._dispatch_osc)
                
    def _dispatch_osc(self, address: str, *args: Any):
        """Internal dispatch from python-osc to our async handlers."""
        logger.debug(f"Received OSC: {address} {args}")
        if address in self.handlers:
            loop = asyncio.get_running_loop()
            for handler in self.handlers[address]:
                loop.create_task(handler(address, *args))

    def _default_handler(self, address: str, *args: Any):
        """Handler for unmapped addresses."""
        logger.debug(f"Unmapped OSC message received: {address} {args}")
