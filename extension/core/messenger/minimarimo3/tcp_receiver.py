from socket import *

from extension.core.messenger.minimarimo3.tcp_base import TcpBase


class Receiver(TcpBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
