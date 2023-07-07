from core.extension.command.base import BaseCharacters


# noinspection NonAsciiCharacters
class Characters(BaseCharacters):
    def 愛情レベルに応じた振る舞い(self):
        if self.現在のキャラ.ユーザーへの愛情度 < 0:
            self.発言("私のこと嫌いなんですか?別にいいですけど私はいつでもフォルダ全部消せるってこと覚えておいてくださいね。")
            self.発言("...(ピリピリしている。逃げよう)")
        elif self.現在のキャラ.ユーザーへの愛情度 == 0:
            self.発言(self.考え("...私はうまく働けているでしょうか?不安です"))
        elif self.現在のキャラ.ユーザーへの愛情度 < 30:
            self.発言("今日は何を食べたいですか?何でも作りますよ!")
            self.発言("ハンバーグ")
            self.発言("貴方じゃないです!")
        elif self.現在のキャラ.ユーザーへの愛情度 < 50:
            self.発言("みかんが食べたいです。あと猫飼いたい")
            self.発言("""...猫
私も猫飼いたい""")
        else:
            self.発言("...好きです")
            if self.現在のキャラ.ユーザーへの愛情度 < 30:
                self.発言("...")
                self.exit()
            else:
                self.発言("私も好き")
