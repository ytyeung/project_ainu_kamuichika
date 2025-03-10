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
Translate the following text from Japanese to Chinese. The original text is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original Japanese meaning accurately. Use modern Chinese. Display in Traditional Chinese.
If a term cannot be translated, keep the original language.

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
小オキキリムイ親自吟唱的歌謠
「クツニサ クトンクトン」

クツニサ クトンクトン
在某一天，我前往水源地遊玩，
發現水源邊有個小矮人，
正彎著腰，一下又一下地敲打著，
想用胡桃木搭建魚梁。
他看見了我，便說道：
「你是誰？我的姪子啊，幫我個忙吧。」
我仔細一看，那魚梁竟是用胡桃木做的，
胡桃木的汁液，混著混濁的水流淌而下，
鮭魚們想逆流而上，卻厭惡胡桃木的味道，
哭泣著，轉身離去。我頓時怒火中燒，
一把奪過小矮人手中敲打木樁的槌子，
朝著他的腰椎中央，
狠狠地敲了下去，發出「砰」的一聲巨響。
我將小矮人的腰椎打斷，殺死了他，
並將他踢入了地獄深淵。我試著搖晃他用胡桃木做的木樁，
似乎一直延伸到了第六層地獄的彼方。
於是，我用盡腰部的力量，全身的力氣，
將那木樁從根部徹底折斷，
也將它踢入了地獄之中。
水源恢復了清澈，清新的風，清澈的水，
流淌而下，那些原本哭泣著離去的
鮭魚們，在清風和清水的滋潤下，
恢復了活力，牠們歡欣鼓舞，嬉戲玩耍，
拍打著水花，奮力向上游去。
我看到這一幕，感到十分欣慰，
便沿著河流，踏上了歸途。這就是
小オキキリムイ所講述的故事。
```
