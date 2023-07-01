from threading import Thread


from core.extension.prefernce.data import ReceiverData
from core.extension.prefernce.loader import load_receiver
from core.hook.hook import hook
from core.messenger.base import Base


class Receiver(Base):
    def __init__(self, data: ReceiverData):
        super().__init__()
        self._receiver = load_receiver(data)

    @hook
    def read(self, **arg) -> bytes:
        return self._receiver.read(**arg)

    @hook
    def write(self, contents: bytes, **kwargs) -> None:
        self._receiver.write(**kwargs)

    @hook
    def communicate(self) -> None:
        Thread(target=self._receiver.communicate).start()
