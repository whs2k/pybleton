import asyncio
import logging
from typing import Optional
from .transport import Transport, OSCTransport
from .lom.liveset import LiveSet, LiveSetModel

logger = logging.getLogger(__name__)

class Pybleton:
    """Main entrypoint for the Pybleton SDK."""
    
    def __init__(self, transport: Transport):
        self.transport = transport
        self.set: Optional[LiveSet] = None
        
    @classmethod
    async def connect(cls, host: str = "127.0.0.1", send_port: int = 11000, recv_port: int = 11001) -> "Pybleton":
        """Connect to Ableton Live using the default OSC transport."""
        transport = OSCTransport(host, send_port, recv_port)
        await transport.connect()
        
        client = cls(transport)
        
        # We simulate querying the initial state. In a real AbletonOSC scenario, 
        # we'd request the state and wait for responses to build the LiveSet model.
        # For this skeleton, we'll initialize an empty or mock state.
        
        # client.set = await client.get_initial_state()
        return client

    async def disconnect(self):
        """Disconnect the transport."""
        await self.transport.disconnect()
        
    async def get_initial_state(self) -> LiveSet:
        # TODO: Implement full state query
        # This would send an OSC message like /live/song/get/num_tracks
        # and wait for the response to build the initial hierarchy.
        pass
