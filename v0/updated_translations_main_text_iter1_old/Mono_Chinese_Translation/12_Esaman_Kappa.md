# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

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
You are translating the following Japanese text into Chinese. The original text is a chant sung by god telling his story. You already have an initial Chinese translation.

Here are your tasks:

1. Compare and criticise the Chinese translation based on the Japanese text. 
3. Improve the Chinese translation based on the comparison results.

Keep the original meanings. Display in Traditional Chinese. If a term cannot be translated, keep the original language.

This is the Japanese text.
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

This is the Chinese translation.
水獺自唱的歌謠
「河童 咧嗚咧嗚 河童」

河童 咧嗚咧嗚 河童
有一天,我沿著河流嬉戲,
游到薩瑪雲庫魯的
汲水路口時,
看見薩瑪雲庫魯的妹妹,像神一般美麗,
一手提著水桶,一手
拿著香蒲束走來,
我便只露出頭在河邊,
問道:「妳有父親嗎?
妳有母親嗎?」
那女孩嚇了一跳,眼睛四處張望,
發現了我,臉上露出
憤怒的表情,
說:「啊,可惡的扁頭,壞扁頭
竟敢愚弄人。狗兒們,過來......」
話音未落,大狗們就
衝了過來,對著我齜牙咧嘴。
我嚇了一跳,趕緊潛入河底,
直接沿著河底逃走了。
然後,我又在奧基基里穆伊的汲水路口
只露出頭來
看見奧基基里穆伊的妹妹,
像神一般美麗,一手提著水桶,
一手拿著香蒲束走來,
我就問她:
「妳有父親嗎?
妳有母親嗎?」
那女孩嚇了一跳,眼睛四處張望,
發現了我,臉上露出
憤怒的表情,
說:「啊,可惡的扁頭,壞扁頭
竟敢愚弄人。狗兒們,過來......」
話音未落,大狗們就衝了過來。
我看到這情景,想起剛才的事,
覺得好笑,正想潛入河底
逃走,
沒想到狗兒們竟然會做出那種事,
牠們齜牙咧嘴地
跳入河底,撲向我,
把我拖到岸上,我的頭和身體
都被牠們咬住、撕扯,最後
發生了什麼事,我就不知道了。
突然回過神來,
發現自己正坐在
一隻大水獺的兩隻耳朵之間。
我知道薩瑪雲庫魯和奧基基里穆伊
都沒有父母,
我還那樣惡作劇,所以受到了懲罰,
被奧基基里穆伊的狗兒們殺死,
落得一個無聊的死法,糟糕的死法。
今後的水獺們啊,千萬不要再惡作劇了。
水獺這樣講述著。


```

### Output
```
水獺自唱的歌謠
「河童 咧嗚咧嗚 河童」

河童 咧嗚咧嗚 河童
有一天，我沿著河流嬉戲，
游到薩瑪雲庫魯的
汲水處時，
看見薩瑪雲庫魯的妹妹，宛如女神般美麗動人，
一手提著水桶，一手
拿著香蒲束走來，
我便只露出頭在河邊，
問道：「妳有父親嗎？
妳有母親嗎？」
那女孩嚇了一跳，眼睛四處張望，
發現了我，臉上頓時
露出憤怒的表情，
說：「啊，可惡的扁頭，壞扁頭
竟敢愚弄人。狗兒們，上啊......」
話音未落，大狗們就
衝了過來，對著我齜牙咧嘴。
我嚇了一跳，趕緊潛入河底，
直接沿著河底逃走了。
然後，我又在奧基基里穆伊的汲水處
只露出頭來，
看見奧基基里穆伊的妹妹，
同樣有著女神般的美麗容貌，一手提著水桶，
一手拿著香蒲束走來，
我就問她：
「妳有父親嗎？
妳有母親嗎？」
那女孩嚇了一跳，眼睛四處張望，
發現了我，臉上頓時
露出憤怒的表情，
說：「啊，可惡的扁頭，壞扁頭
竟敢愚弄人。狗兒們，上啊......」
話音未落，大狗們就衝了過來。
我看到這情景，想起剛才的事，
覺得好笑，正想潛入河底
逃走，
沒想到狗兒們竟然會做出那種事，
牠們齜牙咧嘴地
跳入河底，撲向我，
把我拖到岸上，我的頭和身體
都被牠們撕咬，最後
發生了什麼事，我就不知道了。
突然回過神來，
發現自己正坐在
一隻大水獺的兩隻耳朵之間。
我知道薩瑪雲庫魯和奧基基里穆伊
都是沒有父母的，
我還如此惡作劇，才會受到懲罰，
被奧基基里穆伊的狗兒們殺死，
落得如此可悲的下場。 
今後的水獺們啊，切記不可再惡作劇了。
水獺這樣講述著。

The original translation is generally good, but some phrases can be improved for better flow and accuracy. Specifically, I will focus on refining the descriptions of the girls' beauty, the otter's actions, and the overall narrative to enhance the storytelling in Chinese.

1.  "像神一般美麗" (like a god, beautiful) can be more elegantly expressed.
2.  The repetition of actions can be streamlined for better readability.
3.  The ending can be slightly adjusted to emphasize the moral of the story.
```

