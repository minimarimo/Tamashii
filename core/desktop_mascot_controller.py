from core.extension.prefernce.data import PreferenceData
from core.extension.scenario.data import LoadedScenarioData
from core.messenger.messenger import Messenger
from core.extension.prefernce.loader import load_hook
from core.extension.scenario.loader import load_scenario


class DesktopMascotController:
    """
    デスクトップマスコットの全て。ここで何もかもコントロールする
    """
    hooks: dict[str, list[staticmethod]]
    """拡張機能で実装された関数が格納されています"""
    scenario: LoadedScenarioData
    """キャラの発言タイミングとその内容が格納されています"""

    def __init__(self, preference: PreferenceData):
        DesktopMascotController.hooks = load_hook(preference.extension.hook)
        self._preference = preference
        """拡張のために実装された関数を格納する"""
        self._messenger = Messenger(preference.core.messenger)
        # self._ui = load_ui(preference.core.ui)
        # self._model = load_model(preference.extension.model)
        DesktopMascotController.scenario = load_scenario(preference.extension.scenario)

    @classmethod
    def get_scenario(cls, name: str) -> LoadedScenarioData:
        """
        キャラの発言タイミングとその内容を返します
        """
        return cls.scenario

    def start(self):
        """
        デスクトップマスコットの起動
        """
        self._messenger.communicate()
