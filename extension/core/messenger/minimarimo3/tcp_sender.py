from core.messenger.base import Base


class Sender(Base):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.host = kwargs["host"]
        self.port = kwargs["port"]

    def read(self, **arg) -> bytes:
        pass

    def write(self, message: bytes, **arg) -> None:
        pass

    def communicate(self) -> None:
        print("Sender run!")
