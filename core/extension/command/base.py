# noinspection NonAsciiCharacters
class BaseCharacters:

    def __init__(self):
        pass

    def 考え(self, contents: str) -> str:
        return "<think>"+contents+"</think>"

    def 発言(self, contents: str, target: str = None) -> object:
        """
        キャラに発言させる
        :param contents: 発言内容
        :param target: 会話するキャラ。Noneの場合は現在のキャラ
        """
        pass
