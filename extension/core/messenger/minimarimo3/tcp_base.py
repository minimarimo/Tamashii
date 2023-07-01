from io import TextIOWrapper
from socket import *
from typing import Optional

from core.messenger.base import Base


class TcpBase(Base):
    def __init__(self, **kwargs):
        super().__init__()
        self.host = kwargs["host"]
        self.port = kwargs["port"]
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.fd: Optional[TextIOWrapper] = None
        self._raw_response = b""
        self._raw_message = b""

    def is_available(self) -> bool:
        return not self.fd or self.fd.closed

    def connect(self):
        self.sock.connect((self.host, self.port))
        self.fd = self.sock.makefile("rw", encoding="utf-8")

    def read(self, **kwargs) -> bytes:
        if not self.fd:
            raise Exception("not connected")
        self._raw_response = self.fd.readline().encode("utf-8")
        return self._raw_response

    def write(self, message: bytes, **kwargs) -> None:
        if not self.fd:
            raise Exception("not connected")
        self._raw_message = message
        self.fd.write(message.decode("utf-8"))
        self.fd.flush()

    def communicate(self) -> None:
        print(f"connect to {self.host}:{self.port}")
        self.sock.connect((self.host, self.port))
        with self.sock.makefile("rw", encoding="utf-8") as f:
            while not f.closed:
                message = f"Hello! from{self.__class__.__name__}\n"
                self.write_str(message, fd=f)
                response = self.read_str(fd=f)
                print(f"received: {response}")
