import tomllib
from core.extension.scenario.data import LoadedScenarioData
from core.extension.prefernce.data import ScenarioData
from core.extension.loader import load_dataclass_from_dict


def load_scenario(scenario_preferences: list[ScenarioData]) -> LoadedScenarioData:
    scenario = {}
    for preference in scenario_preferences:
        with open(f"./extension/scenario/{preference.path}", "rb") as f:
            # tomllibのload関数は内容をdecodeするので、デフォのUTF-8でないと文字化けする
            # まあ規格通りのTOMLであればUnicode(UTF-8)であることが保証されているので、別にいいかな
            preference_contents = tomllib.load(f)
            for scenario_name, scenario_contents in preference_contents.items():
                if ("message" in scenario_contents.keys()) and (scenario_name not in scenario.keys()) :
                    scenario[scenario_name] = []
                scenario[scenario_name] += scenario_contents["message"]

    return load_dataclass_from_dict(LoadedScenarioData, scenario)
