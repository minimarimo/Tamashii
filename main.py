import json  # loadに使う

from core.extension.prefernce.data import PreferenceData, from_dict
from core.desktop_mascot_controller import DesktopMascotController


if __name__ == "__main__":
    # こいつは俺が整理するために書いてる設定ファイルであって、SettingsDataの形式に則っていればなんでもいい
    # スマホでユーザーにjsonを編集させることを強制すべきではないので、実際はGUIでの選択&編集を想定している
    #   その場合、GUIでの選択&編集をした結果をjsonに書き込む必要がある。それはsettings/Userに書き込む
    # preference.jsonはautherを読み込み自動でロード ← ユーザー名被ったらどうすんの?
    SETTINGS_PATH = "extension/preference/minimarimo3/example.json"
    with open(SETTINGS_PATH, "r", encoding="UTF-8") as f:
        contents = json.load(f)
        settings_data = from_dict(PreferenceData, contents)

    desktop_mascot_controller = DesktopMascotController(settings_data)
    desktop_mascot_controller.start()
