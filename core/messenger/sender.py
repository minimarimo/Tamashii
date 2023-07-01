from threading import Thread


from core.extension.prefernce.data import SenderData
from core.extension.prefernce.loader import load_sender
from core.hook.hook import hook
from core.messenger.base import Base


class Sender(Base):
    def __init__(self, data: SenderData):
        super().__init__()
        self._sender = load_sender(data)

    def is_available(self) -> bool:
        return self._sender.is_available()

    @hook
    def write(self, contents: bytes, **kwargs) -> bytes:
        return self._sender.write(contents, **kwargs)

    @hook
    def read(self, **arg) -> bytes:
        return self._sender.read(**arg)

    @hook
    def connect(self) -> None:
        self._sender.connect()
