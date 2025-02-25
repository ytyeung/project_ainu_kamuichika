# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Pon Okikirmui yaieyukar, “Kutnisa kutunkutun” 小オキキリムイが自ら歌った謡「クツニサ クトンクトン」

### Model
gemini-2.0-flash-001

### Setting
```
generate_content_config = types.GenerateContentConfig(
    temperature = 0,
    top_p = 0,
    max_output_tokens = 8192,
    response_modalities = ["TEXT"],
    safety_settings = [types.SafetySetting(
      category="HARM_CATEGORY_HATE_SPEECH",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_DANGEROUS_CONTENT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
      threshold="OFF"
    ),types.SafetySetting(
      category="HARM_CATEGORY_HARASSMENT",
      threshold="OFF"
    )],
    system_instruction=[types.Part.from_text(text=si_text1)],
  )
```

### System prompt
```
You are a professional translator. You know Japanese, English and Chinese. You can translate Japanese into either Chinese or English.
```

### Prompt
```
Translate the following text from Japanese to Chinese. The original text is a poem. Try to make the translation poetic but keep the original meanings. Display in Traditional Chinese.

小オキキリムイが自ら歌った謡
「クツニサ クトンクトン」

クツニサ クトンクトン
ある日に水源の方へ遊びに
出かけたら,水源に一人の小男が
胡桃くるみの木の簗やなをたてるため杭を打つのに
腰を曲げ曲げしている.
私を見ると,いう事には,
「誰だ? 私の甥よ,私に手伝ってお呉れ.」
という.見ると,胡桃の簗
なものだから,胡桃の水,濁った水
が流れて来て鮭どもが
上って来ると胡桃の水が嫌なので
泣きながら帰ってゆく.私は腹が立ったので
小男の持っている杭を打つ槌を
引ったくり小男の腰の央を
私がたたく音がポンと響いた.小男の
腰の央を折ってしまって殺してしまい
地獄へ踏み落してやった.彼の胡桃の杭を
揺り動かして見ると六つの地獄の
彼方まで届いている様だ.
それから,私は腰の力,からだ中の力を
出して,その杭を根本から
折ってしまい,地獄へ踏み落してしまった.
水源から清い風,清い水が
流れて来て,泣きながら帰って行った.
鮭どもは清い風,清い水に
気を恢復して,大さわぎ大笑いして遊び
ながら,パチャパチャと
上って来た.私はそれを見て,安心をし
流れに沿うて帰って来た.と
小さいオキキリムイが物語った.
```

### Output
```
好的，以下是將日文詩歌翻譯成繁體中文的譯文，力求保持原意並兼顧詩意：

小オキキリムイ自歌之謠

「クツニサ クトンクトン」

クツニサ クトンクトン
某日嬉遊溯水源，
見一侏儒彎腰忙，
築堰胡桃立木樁。
見我問曰：「汝為誰？
吾之甥也助吾為。」
觀其所築胡桃堰，
胡桃之水濁且渾，
鮭魚逆流至此間，
厭惡濁水涕漣漣，
悲鳴迴首返故園。
吾怒奪其擊樁槌，
猛擊侏儒腰中央，
「砰」然一聲震四方。
侏儒腰斷命已喪，
一腳踢入幽冥鄉。
搖其胡桃之木樁，
直達六獄之遠方。
吾奮全身之力氣，
連根折斷此木樁，
踢入地獄永不揚。
水源清風徐徐來，
水源清水潺潺流，
鮭魚不再淚滿腮。
清風清水滌塵埃，
精神煥發樂開懷，
嬉戲逐浪溯流上，
拍水之聲滿山崖。
見此情景吾心安，
沿溪而歸賦歸帆。

小オキキリムイ如是言。

**一些翻譯說明：**

*   **保留原文意象：** 盡可能保留了原文中的意象，例如胡桃、鮭魚、地獄等，以保持原文的風味。
*   **詩意化處理：** 在不影響原意的基礎上，對部分詞句進行了詩意化的處理，例如將「遊びに出かけたら」翻譯為「嬉遊溯水源」，更顯雅致。
*   **語氣調整：** 盡量模擬了詩歌的語氣，使用了一些較為古雅的詞彙，例如「汝」、「吾」等。
*   **斷句考量：** 斷句方面，力求符合中文詩歌的節奏感，使譯文更易於吟誦。

希望這個譯文能讓您滿意。

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to Chinese. Keep the original meanings. Display in Traditional Chinese.
```

### Output of this prompt

```
好的，以下是將日文翻譯成繁體中文的結果，並儘可能保留原文含義：

小オキキリムイ（小奧奇基利穆伊）自己唱的歌謠
「クツニサ クトンクトン」

クツニサ クトンクトン
有一天，我到水源地去玩
出發後，在水源地看到一個小矮人
為了建造胡桃木的魚梁，正在打樁
彎著腰。
他看到我，就說：
「你是誰？我的姪子啊，幫我一下。」
我看見，因為是胡桃木的魚梁
所以胡桃水、混濁的水
流過來，鮭魚們
要往上游時，因為討厭胡桃水
就哭著回去了。我非常生氣
搶走了小矮人拿著的打樁槌
敲打小矮人的腰部中央
我敲下去的聲音「砰」地響起。小矮人的
腰部中央被我打斷，把他殺了
把他踹進地獄。搖動他的胡桃木樁
看起來好像延伸到六層地獄的
彼端。
然後，我用腰部的力量、全身的力量
從根本上
折斷了那根木樁，把他踹進地獄。
從水源流出清新的風、清澈的水
哭著回去的
鮭魚們，因為清新的風、清澈的水
恢復了精神，非常熱鬧、大聲歡笑地玩耍
一邊拍打著水面
一邊往上游。我看到那樣，就安心了
沿著水流回家了。
小奧奇基利穆伊這樣講述著。

```