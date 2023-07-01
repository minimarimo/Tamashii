import json  # loadに使う

from core.extension.prefernce.data import PreferenceData
from core.extension.loader import load_dataclass_from_dict
from core.desktop_mascot_controller import DesktopMascotController


if __name__ == "__main__":
    # こいつは俺が整理するために書いてる設定ファイルであって、SettingsDataの形式に則っていればなんでもいい
    # スマホでユーザーにjsonを編集させることを強制すべきではないので、実際はGUIでの選択&編集を想定している
    #   その場合、GUIでの選択&編集をした結果をjsonに書き込む必要がある。それはsettings/Userに書き込む
    # preference.jsonはautherを読み込み自動でロード ← ユーザー名被ったらどうすんの?
    SETTINGS_PATH = "extension/preference/minimarimo3/example.json"
    with open(SETTINGS_PATH, "r", encoding="UTF-8") as f:
        settings_data = load_dataclass_from_dict(PreferenceData, json.load(f))

    desktop_mascot_controller = DesktopMascotController(settings_data)
    desktop_mascot_controller.start()
