from threading import Thread


from core.extension.prefernce.data import ReceiverData
from core.extension.prefernce.loader import load_receiver
from core.hook.hook import hook
from core.messenger.base import Base


class Receiver(Base):
    def __init__(self, data: ReceiverData):
        super().__init__()
        self._receiver = load_receiver(data)

    def is_available(self) -> bool:
        return self._receiver.is_available()

    @hook
    def read(self, **kwarg) -> bytes:
        return self._receiver.read(**kwarg)

    @hook
    def write(self, contents: bytes, **kwargs) -> None:
        self._receiver.write(contents, **kwargs)

    @hook
    def connect(self) -> None:
        self._receiver.connect()
