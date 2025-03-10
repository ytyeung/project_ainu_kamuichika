# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Pipa yaieyukar, “Tonupeka ranran” 沼貝が自ら歌った謡「トヌペカ ランラン」

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

沼貝が自ら歌った謡「トヌペカ ランラン」

トヌペカ ランラン
強烈な日光に私の居る所も
乾いてしまって今にも私は死にそうです.
「誰か,水を飲ませて下すって
助けて下さればいい.水よ水よ」と私たちが泣き叫んで
いますと,ずーっと浜の方から一人の女が
籠を背負って来ています.
私たちは泣いていますと,私たちの傍を通り
私たちを見ると,
「おかしな沼貝,悪い沼貝,何を泣いて
うるさい事さわいでいるのだろう.」と言って
私たちを踏みつけ,足先にかけ飛ばし,貝殻と共につぶして
ずーっと山へ行ってしまいました.
「おお痛,苦しい,水よ水よ.」と泣き叫んで
いると,ずっと浜の方からまた一人の女が
籠を背負って来ています.私たちは
「誰か私たちに水を飲ませて助けて下さるといい,
おお痛,おお苦しい,水よ水よ.」と叫び泣きました
すると,娘さんは,神の様な美しい気高い様子で
私の側へ来て私たちを見ると,
「まあかわいそうに,大へん暑くて沼貝たちの
寝床も乾いてしまって水を欲しがって
いるのだね,どうしたのでしょう
何だか踏みつけられでもした様だが......」と言いつつ
私たちみんなを拾い集めて蕗の葉に
入れて,きれいな湖に入れてくれました.
清い冷水でスッカリ元気を恢復し
大へん丈夫になりました.そこで始めて
かの女たちの気性を探って
見ると,先に来て,私を踏みつぶした
にくらしい女,わるい女はサマユンクルの
妹で,私たちを憫み
助けて下さった若い娘さん淑しとやかな方
は,オキキリムイの妹なのでありました.
サマユンクルの妹は悪にくらしいので
その粟畑を枯らしてしまい,オキキリムイの
妹のその粟畑をばよく実らせました.
その年に,オキキリムイの妹は大そう多く収穫をしました.
私の故為せいでそうなった事を知って
沼貝の殻で粟の穂を摘みました.
それから,毎年,人間の女たちは
栗の穂を摘む時は沼貝の殻を使う様になったのです.
と,一つの沼貝が物語りました.
```

### Output
```
好的，這是一段將日文詩歌翻譯成繁體中文的嘗試，我會盡力在保留原意的同時，兼顧詩意：

**沼貝自歌謠「托努佩卡 蘭蘭」**

托努佩卡 蘭蘭

烈日炎炎，灼我身旁，
乾涸將盡，命不久長。
「誰人賜水，解我乾渴，
救我脫離，此般苦厄。
水啊水啊！」哀聲泣訴，
遙見海濱，一女緩步。
背負竹簍，向我走來，
無視哀鳴，漠然走開。
見我可憐，
「可憎沼貝，何苦喧嘩，
擾人清靜，徒增笑話。」
言罷足踏，碾碎貝殼，
拋擲遠方，揚長而去。
「痛哉苦哉，水啊水啊！」
哀號未絕，又見一女，
背負竹簍，自海濱來。
我等呼號：「誰人慈悲，
賜我甘霖，救我將死。
痛哉苦哉，水啊水啊！」
此女若神，容顏清麗，
見我慘狀，駐足嘆息：
「可憐沼貝，酷暑難耐，
棲身之所，乾涸龜裂，
渴求甘霖，何故遭難，
莫非受人，踐踏欺凌？」
輕柔拾起，聚攏一處，
置於蕗葉，捧入清湖。
清冽湖水，滋潤身軀，
重獲生機，恢復元氣。
方知二女，性情迥異，
先來之女，狠心踐踏，
乃是薩瑪雲庫爾之妹，
後至之女，憐憫相助，
乃是奧奇奇里姆伊之妹。
薩瑪雲庫爾之妹，心懷惡念，
致使粟田，枯萎凋零。
奧奇奇里姆伊之妹，心懷善念，
使其粟田，豐收盈倉。
是年，奧奇奇里姆伊之妹，
收穫頗豐，皆因我故。
遂以沼貝之殼，摘取粟穗。
自此之後，人間女子，
採摘粟穗，皆用貝殼。

一沼貝如是說。

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to Chinese. Keep the original meanings. Display in Traditional Chinese.
```

### Output of this prompt

```
以下是將日文文本翻譯成繁體中文的結果：

沼貝自唱的歌謠「托努佩卡 蘭蘭」

托努佩卡 蘭蘭
強烈的日光照射，我的棲身之處也
乾涸了，我快要死了。
「誰來給我水喝，
救救我吧。水啊水啊」我們哭喊著，
從遠方的海灘走來一位女子，
背著竹簍。
我們哭泣著，她從我們身旁經過，
看見我們，
說：「可笑的沼貝，可惡的沼貝，哭什麼
吵吵鬧鬧的。」
她踩踏我們，用腳尖踢開，連同貝殼一起踩碎，
然後就往山裡去了。
「好痛，好難受，水啊水啊。」我們哭喊著，
從遠方的海灘又走來一位女子，
背著竹簍。我們
「誰來給我們水喝，救救我們吧，
好痛，好難受，水啊水啊。」哭喊著。
於是，那位姑娘，神一般美麗高貴，
來到我們身邊，看見我們，
說：「真可憐，天氣這麼熱，沼貝們的
棲身之處都乾涸了，想要喝水，
這是怎麼了呢？
好像是被踩踏過一樣……」
她一邊說著，一邊把我們都撿起來，
放在蕗葉上，放進了清澈的湖裡。
我們喝了清澈的冷水，完全恢復了元氣，
變得非常健康。於是，我們開始
探究那些女子的性情，
發現先來，踩踏我的
可憎的女子，壞女人是薩瑪雲庫爾的
妹妹，而憐憫我們，
幫助我們的年輕姑娘，溫柔賢淑的
是奧基基里穆伊的妹妹。
薩瑪雲庫爾的妹妹邪惡可憎，
導致她的粟米田枯萎，而奧基基里穆伊的
妹妹的粟米田則結實纍纍。
那一年，奧基基里穆伊的妹妹大豐收。
她知道這是因為我的緣故，
就用沼貝的殼來摘粟米的穗。
從那以後，每年，人類的女子們
在摘粟米穗的時候，都會使用沼貝的殼。
一隻沼貝這樣講述著。

```