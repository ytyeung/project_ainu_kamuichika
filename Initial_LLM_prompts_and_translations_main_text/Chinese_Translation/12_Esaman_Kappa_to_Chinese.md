# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Esaman yaieyukar, “Kappa reureu kappa” 獺かわうそが自ら歌った謡「カッパ レウレウ カッパ」

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

獺かわうそが自ら歌った謡
「カッパ レウレウ カッパ」

カッパ レウレウ カッパ
ある日に,流れに沿うて遊びながら
泳いで下りサマユンクルの
水汲路のところに来ると,
サマユンクルの妹が神の様な美しい容子で
片手に手桶を持ち片手に
蒲の束を持って来ているので
川の縁に私は頭だけ出し,
「お父様をお持ちですか?
お母様をお持ちですか?」と云うと,
娘さんは驚いて眼をきょろきょろさせ
私を見つけると,怒の色を顔に
現して,
「まあ,にくらしい扁平頭,悪い扁平頭が
人をばかにして.犬たちよ,ココ......」
と言うと,大きな犬どもが
駈け出して来て,私を見ると牙を鳴ら
している.私はビックリして川の底へ
潜り込んで直ぐそのまま川底を通って
逃げ下った.
そうして,オキキリムイの水汲路の
川口へ頭だけだして
見ると,オキキリムイの妹が
神の様に美しい様子で片手に手桶を持ち
片手に蒲の束を持って
来たので私のいうことには,
「御父様をお持ちですか?
御母様をお持ちですか?」というと,
娘さんは驚いて眼をきょろきょろさせ
私を見ると,怒りの色を顔に
表して,
「まあ,にくらしい扁平頭,悪い扁平頭が
人をばかにして.犬たちよ,ココ......」
と言うと大きな犬どもが駈け出して来た.
それを見て私は先刻の事を思い出し
可笑しく思いながら川の底へ
潜りこんで逃げようとしたら,
まさか犬たちがそんな事をしようとは
思わなかったのに,牙を鳴らしながら
川の底まで私に飛び付き
陸へ私を引き摺り上げ,私の頭も私の体も
噛みつかれ噛みむしられて,しまいに
どうなったかわからなくなってしまった.
ふと気が付いて見ると,
大きな獺の耳と耳の間に私はすわって
いた.
サマユンクルもオキキリムイも
父もなく母もないのを私は知って
あんな悪戯をしたので罰を当てられ
オキキリムイの犬どもに殺され
つまらない死方,悪い死方をするのです.
これからの獺たちよ,決して悪戯をしなさるな.
と,獺が物語った.
```

### Output
```
水獺自歌之謠
「卡帕 留留 卡帕」

卡帕 留留 卡帕
某日，我沿著溪流嬉戲而下，
來到薩瑪雲庫魯（Samayunkuru）的汲水路。
薩瑪雲庫魯的妹妹，如神祇般美麗，
一手提著水桶，一手拿著香蒲。
我只露出頭在河邊，問道：
「妳有父親嗎？妳有母親嗎？」

那少女驚訝地睜大眼睛，四處張望，
發現了我，臉上頓時充滿怒色，
「啊，可憎的扁頭，惡劣的扁頭，
竟敢愚弄人！狗兒們，上啊……」

話音未落，幾隻巨犬便衝了出來，
對著我齜牙咧嘴。我嚇了一跳，
立刻潛入河底，沿著河床逃走了。

接著，我又在奧奇基里穆伊（Okikirmui）的汲水路，
只露出頭來。
奧奇基里穆伊的妹妹，同樣如神祇般美麗，
一手提著水桶，一手拿著香蒲。
我便問道：
「妳有父親嗎？妳有母親嗎？」

那少女驚訝地睜大眼睛，四處張望，
發現了我，臉上頓時充滿怒色，
「啊，可憎的扁頭，惡劣的扁頭，
竟敢愚弄人！狗兒們，上啊……」

話音未落，幾隻巨犬便衝了出來。

我見狀，想起方才的遭遇，
覺得十分可笑，正要潛入河底逃走，
沒想到那些狗竟然也跟著跳了下來，
對著我狂吠，並撕咬。
將我拖上岸，我的頭和身體
被牠們啃咬撕扯，最後我完全失去了意識。

突然，我醒了過來，
發現自己正坐在
一隻巨大的水獺的雙耳之間。

我明知薩瑪雲庫魯和奧奇基里穆伊
都沒有父母，卻還故意戲弄她們，
因此受到了懲罰，
被奧奇基里穆伊的狗殺死，
落得如此無聊、可悲的下場。

今後的水獺們啊，千萬不要再惡作劇了。

水獺如此講述著。
```
