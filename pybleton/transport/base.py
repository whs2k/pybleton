from abc import ABC, abstractmethod
from typing import Callable, Any, Awaitable

HandlerFunc = Callable[..., Awaitable[None]]

class Transport(ABC):
    """Abstract base class for communicating with Ableton Live."""
    
    @abstractmethod
    async def connect(self):
        """Connect to the DAW."""
        pass

    @abstractmethod
    async def disconnect(self):
        """Disconnect from the DAW."""
        pass

    @abstractmethod
    async def send(self, address: str, *args: Any):
        """Send a message to the DAW."""
        pass

    @abstractmethod
    def add_handler(self, address: str, handler: HandlerFunc):
        """Register a handler for incoming messages."""
        pass

    @abstractmethod
    def remove_handler(self, address: str, handler: HandlerFunc):
        """Unregister a handler."""
        pass
