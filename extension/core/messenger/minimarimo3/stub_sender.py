from core.messenger.base import Base


class Sender(Base):
    def __init__(self, **kwargs):
        super().__init__()
        self._raw_response = b""
        self._raw_message = b""

    def is_available(self) -> bool:
        return True

    def connect(self):
        pass

    def read(self, **kwargs) -> bytes:
        return b"""{"command":"message","args":{"status":"OK"}}"""

    def write(self, message: bytes, **kwargs) -> None:
        pass
