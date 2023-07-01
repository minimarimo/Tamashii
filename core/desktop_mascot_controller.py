from core.extension.prefernce.data import PreferenceData
from core.messenger.messenger import Messenger
from core.extension.prefernce.loader import load_hook


class DesktopMascotController:
    """
    デスクトップマスコットの全て。ここで何もかもコントロールする
    """
    hooks: dict[str, list[staticmethod]]
    """拡張機能で実装された関数が格納されています"""

    def __init__(self, preference: PreferenceData):
        DesktopMascotController.hooks = load_hook(preference.extension.hook)
        self._preference = preference
        """拡張のために実装された関数を格納する"""
        self._messenger = Messenger(preference.core.messenger)
        # self._ui = load_ui(preference.core.ui)
        # self._model = load_model(preference.extension.model)
        # self._scenario = load_scenario(preference.extension.scenario)

    def start(self):
        """
        デスクトップマスコットの起動
        """
        self._messenger.communicate()
