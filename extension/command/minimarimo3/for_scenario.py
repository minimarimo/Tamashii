from core.extension.command.base import BaseCharacters


class Characters(BaseCharacters):
    @staticmethod
    def 愛情レベルに応じた振る舞い(cls):
        if cls.現在のキャラ.ユーザーへの愛情度 < 0:
            cls.発言("私のこと嫌いなんですか?別にいいですけど私はいつでもフォルダ全部消せるってこと覚えておいてくださいね。")
            cls.発言("...(ピリピリしている。逃げよう)")
        elif cls.現在のキャラ.ユーザーへの愛情度 == 0:
            cls.発言(cls.考え("...私はうまく働けているでしょうか?不安です"))
        elif cls.現在のキャラ.ユーザーへの愛情度 < 30:
            cls.発言("今日は何を食べたいですか?何でも作りますよ!")
            cls.発言("ハンバーグ")
            cls.発言("貴方じゃないです!")
        elif cls.現在のキャラ.ユーザーへの愛情度 < 50:
            cls.発言("みかんが食べたいです。あと猫飼いたい")
            cls.発言("""...猫
私も猫飼いたい""")
        else:
            cls.発言("...好きです")
            if cls.現在のキャラ.ユーザーへの愛情度 < 30:
                cls.発言("...")
                cls.exit()
            else:
                cls.発言("私も好き")
