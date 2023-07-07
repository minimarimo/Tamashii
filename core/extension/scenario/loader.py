import tomllib

from core.extension.scenario.data import LoadedScenarioData, MessageData
from core.extension.prefernce.data import ScenarioData
from core.extension.loader import load_dataclass_from_dict


def load_scenario(scenario_preferences: ScenarioData) -> LoadedScenarioData:
    with open(f"./extension/scenario/{scenario_preferences.path}", "rb") as f:
        # tomllibのload関数は内容をdecodeするので、デフォのUTF-8でないと文字化けする
        # まあ規格通りのTOMLであればUnicode(UTF-8)であることが保証されているので、別にいいかな
        scenario = tomllib.load(f)
        """
        for scenario_name, scenario_contents in preference_contents.items():
            if ("message" in scenario_contents.keys()) and (scenario_name not in scenario.keys()) :
                scenario[scenario_name] = []
            scenario[scenario_name] += scenario_contents["message"]
            """

    return load_dataclass_from_dict(LoadedScenarioData, scenario)


def parse_scenario(darty_scenario: list[str], self) -> list[str]:
    """
    IF文や関数などを解析してlist[str]に変換する
    """
    def check_if_statement(if_statement: str) -> bool:
        """
        IF文が正確に書かれているかどうかを判定する
        """
        if not (if_statement.startswith("{IF") and if_statement.endswith("}")):
            print("IF文は{IFで始まり、}で終わる必要があります")
            return False
        if if_statement.count("{") != 1 or if_statement.count("}") != 1:
            print("IF文は一行を占有します")
            return False
        if if_statement.count(",") != if_statement.count(", "):
            print("IF文の中身は\", \"で区切られている必要があります。\",\"の後にスペースを入れてください")
            return False
        return True

    # IF文を解析する。これによってscenarioがList[str]に変換される
    def replace_if_statement(scenario: list[str]) -> list[str]:
        if_index = 0
        formatted_scenario: list[str] = []
        # シナリオを一行ずつ読み込む
        for message in scenario:
            # 前回IF文の解析をした結果取り出すべきメッセージの場所が分かったので取り出す
            if if_index != 0:
                if type(message[if_index]) == str:
                    raise SyntaxError(f"分岐後のテキスト表示に関する誤認が起こりやすいのでIF文の条件分岐後に表示するテキストはそれぞれ\"[]\"で囲ってください。" +
                                      f"\n\t\"{message[if_index]}\" -> [\"{message[if_index]}\"]""")
                for msg in message[if_index]:
                    formatted_scenario.append(msg)
                if_index = 0
                continue

            if "{IF(" in message:
                # IF文が正確であることをチェック
                assert check_if_statement(message)
                # IF文を展開する
                expressions = message[message.find("{IF(") + 4: message.find(")}")].split(", ")
                # 実行
                for expression in expressions:
                    if eval(expression, {}, {"self": self}):
                        if_index = expressions.index(expression)
                        break
                else:
                    if_index = len(expressions)
            else:
                formatted_scenario.append(message)
        return formatted_scenario

    formatted_scenario: list[str] = darty_scenario
    while "{IF" in str(formatted_scenario):
        formatted_scenario = replace_if_statement(formatted_scenario)

    for scenario in formatted_scenario:
        print("シナリオ", scenario)

    # TODO: かっこの中身を実行する
    return formatted_scenario
