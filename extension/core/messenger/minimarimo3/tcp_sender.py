from core.messenger.base import Base

from extension.core.messenger.minimarimo3.tcp_base import TcpBase


class Sender(TcpBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
