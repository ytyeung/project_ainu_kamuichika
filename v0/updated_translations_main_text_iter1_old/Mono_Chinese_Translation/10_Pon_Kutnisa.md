# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

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
You are translating the following Japanese text into Chinese. The original text is a chant sung by god telling his story. You already have an initial Chinese translation.

Here are your tasks:

1. Compare and criticise the Chinese translation based on the Japanese text. 
3. Improve the Chinese translation based on the comparison results.

Keep the original meanings. Display in Traditional Chinese. If a term cannot be translated, keep the original language.

This is the Japanese text.
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

This is the Chinese translation.
小オキキリムイ(小奧奇基利穆伊)自己唱的歌謠
「クツニサ クトンクトン」

クツニサ クトンクトン
有一天,我到水源地去玩
出發後,在水源地看到一個小矮人
為了建造胡桃木的魚梁,正在打樁
彎著腰。
他看到我,就說:
「你是誰?我的姪子啊,幫我一下。」
我看見,因為是胡桃木的魚梁
所以胡桃水、混濁的水
流過來,鮭魚們
要往上游時,因為討厭胡桃水
就哭著回去了。我非常生氣
搶走了小矮人拿著的打樁槌
敲打小矮人的腰部中央
我敲下去的聲音「砰」地響起。小矮人的
腰部中央被我打斷,把他殺了
把他踹進地獄。搖動他的胡桃木樁
看起來好像延伸到六層地獄的
彼端。
然後,我用腰部的力量、全身的力量
從根本上
折斷了那根木樁,把他踹進地獄。
從水源流出清新的風、清澈的水
哭著回去的
鮭魚們,因為清新的風、清澈的水
恢復了精神,非常熱鬧、大聲歡笑地玩耍
一邊拍打著水面
一邊往上游。我看到那樣,就安心了
沿著水流回家了。
小奧奇基利穆伊這樣講述著。


```

### Output
```
小奧奇基利穆伊自己唱的歌謠
「クツニサ クトンクトン」

クツニサ クトンクトン
有一天，我到水源地去玩。
出發後，在水源地看到一個小矮人，
為了建造胡桃木的魚梁，正在彎著腰打樁。
他看到我，就說：
「你是誰？我的姪子啊，幫我一下。」
我看見，因為是胡桃木的魚梁，
所以流過來的是胡桃水，混濁不清。
鮭魚們想要往上游，卻因為厭惡胡桃水的味道，
哭哭啼啼地回去了。我非常生氣，
一把搶過小矮人手中的打樁槌，
朝他腰椎正中央敲去，
我敲下去的聲音「砰」地響起。小矮人的
腰椎被打斷，我便殺了他，
把他踹進地獄。搖動他的胡桃木樁，
看起來好像延伸到六層地獄的彼端。
然後，我用盡腰部和全身的力量，
從根本上折斷了那根木樁，把他踹進地獄。
從水源地流出清新的風、清澈的水，
原本哭著回去的鮭魚們，因為清新的風和清澈的水
恢復了精神，牠們非常熱鬧，歡快地嬉戲，
一邊拍打著水面，一邊往上游。我看到那樣，就安心了，
沿著水流回家了。
小奧奇基利穆伊這樣講述著。

The current translation is generally good, but some areas can be improved for accuracy and naturalness in Chinese. Specifically, the transliteration of "小オキキリムイ" can be refined, and the description of the salmon's reaction to the water can be made more vivid. The phrase "腰の央" can be translated more precisely. Also, the flow of some sentences can be adjusted for better readability in Chinese.
```

