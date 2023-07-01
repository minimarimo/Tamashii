from io import TextIOWrapper
from socket import *

from core.messenger.base import Base


class TcpBase(Base):
    def __init__(self, **kwargs):
        super().__init__()
        self.host = kwargs["host"]
        self.port = kwargs["port"]
        self.sock = socket(AF_INET, SOCK_STREAM)

    def read(self, **kwargs) -> bytes:
        fd: TextIOWrapper = kwargs["fd"]
        return fd.readline().encode("utf-8")

    def write(self, contents: bytes, **kwargs) -> None:
        fd: TextIOWrapper = kwargs["fd"]
        fd.write(contents.decode("utf-8"))
        fd.flush()

    def communicate(self) -> None:
        print(f"connect to {self.host}:{self.port}")
        self.sock.connect((self.host, self.port))
        with self.sock.makefile("rw", encoding="utf-8") as f:
            while not f.closed:
                message = f"Hello! from{self.__class__.__name__}\n"
                self.write_str(message, fd=f)
                response = self.read_str(fd=f)
                print(f"received: {response}")
