from dataclasses import dataclass
from typing import List


@dataclass
class LoadedScenarioData:
    """シナリオの設定がある"""
    # scenario: ScenarioData
    random: List[str]
    on_click: List[str]
