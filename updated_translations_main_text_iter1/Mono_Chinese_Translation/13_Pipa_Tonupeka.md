# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

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
You are translating the following Japanese text into Chinese. The original text is a chant sung by god telling his story. You already have an initial Chinese translation.

Here are your tasks:

1. Compare and criticise the Chinese translation based on the Japanese text. 
3. Improve the Chinese translation based on the comparison results.

Keep the original meanings. Display in Traditional Chinese. If a term cannot be translated, keep the original language.

This is the Japanese text.
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

This is the Chinese translation.
沼貝自唱的歌謠「托努佩卡 蘭蘭」

托努佩卡 蘭蘭
強烈的日光照射,我的棲身之處也
乾涸了,我快要死了。
「誰來給我水喝,
救救我吧。水啊水啊」我們哭喊著,
從遠方的海灘走來一位女子,
背著竹簍。
我們哭泣著,她從我們身旁經過,
看見我們,
說:「可笑的沼貝,可惡的沼貝,哭什麼
吵吵鬧鬧的。」
她踩踏我們,用腳尖踢開,連同貝殼一起踩碎,
然後就往山裡去了。
「好痛,好難受,水啊水啊。」我們哭喊著,
從遠方的海灘又走來一位女子,
背著竹簍。我們
「誰來給我們水喝,救救我們吧,
好痛,好難受,水啊水啊。」哭喊著。
於是,那位姑娘,神一般美麗高貴,
來到我們身邊,看見我們,
說:「真可憐,天氣這麼熱,沼貝們的
棲身之處都乾涸了,想要喝水,
這是怎麼了呢?
好像是被踩踏過一樣......」
她一邊說著,一邊把我們都撿起來,
放在蕗葉上,放進了清澈的湖裡。
我們喝了清澈的冷水,完全恢復了元氣,
變得非常健康。於是,我們開始
探究那些女子的性情,
發現先來,踩踏我的
可憎的女子,壞女人是薩瑪雲庫爾的
妹妹,而憐憫我們,
幫助我們的年輕姑娘,溫柔賢淑的
是奧基基里穆伊的妹妹。
薩瑪雲庫爾的妹妹邪惡可憎,
導致她的粟米田枯萎,而奧基基里穆伊的
妹妹的粟米田則結實纍纍。
那一年,奧基基里穆伊的妹妹大豐收。
她知道這是因為我的緣故,
就用沼貝的殼來摘粟米的穗。
從那以後,每年,人類的女子們
在摘粟米穗的時候,都會使用沼貝的殼。
一隻沼貝這樣講述著。


```

### Output
```
沼貝自唱的歌謠「托努佩卡 蘭蘭」

托努佩卡 蘭蘭
烈日當空，我的居所也乾涸殆盡，奄奄一息。
「誰能給我一口水，
救救我吧！水啊，水啊！」我們哀號著，
遠方海灘走來一位女子，
背著竹簍。
我們哭泣，她從我們身旁經過，
看見我們，
說：「可笑的沼貝，可憎的沼貝，哭哭啼啼，
吵鬧喧嘩！」
她踐踏我們，用腳尖踢開，連同貝殼一同踩碎，
揚長而去，往山裡去了。
「好痛，好苦，水啊，水啊！」我們哀嚎，
遠方海灘又走來一位女子，
背著竹簍。我們
「誰能給我們一口水，救救我們吧！
好痛，好苦，水啊，水啊！」呼喊。
於是，那位姑娘，宛如神祇般美麗莊嚴，
來到我們身邊，看見我們，
說：「真是可憐，天氣如此炎熱，沼貝們的
棲身之所都乾裂了，渴望著水，
這是怎麼回事呢？
似乎是被踐踏過了……」
她一邊說著，一邊將我們一一撿起，
放在蜂斗菜葉上，放入清澈的湖水中。
我們暢飲清冽的湖水，頓時恢復了元氣，
變得非常強壯。於是，我們開始
探究這些女子的性情，
發現先前到來，踐踏我們的
可憎女子，惡毒的女人，是薩瑪雲庫爾的
妹妹；而憐憫我們，
幫助我們的年輕姑娘，溫柔嫻靜的
是奧基基里穆伊的妹妹。
薩瑪雲庫爾的妹妹心術不正，
使得她的粟米田枯萎凋零；而奧基基里穆伊的
妹妹的粟米田則結滿了豐碩的果實。
那一年，奧基基里穆伊的妹妹迎來了大豐收。
她明白這是因為我的緣故，
便用沼貝的殼來收割粟米的穗。
從那以後，每年，人類的女子們
在收割粟米穗的時候，都會使用沼貝的殼。
一隻沼貝如此訴說著。

The original translation is generally good, but some phrases can be improved to be more natural and vivid in Chinese. Also, some terms can be refined for better cultural context and readability. Specifically:

*   "強烈的日光照射,我的棲身之處也乾涸了,我快要死了。" can be more concise and impactful.
*   The repetition of "哭喊著" can be varied for better flow.
*   "神一般美麗高貴" can be enhanced to better convey the divine quality.
*   "蕗葉" can be checked for a more accurate and culturally relevant translation.
*   The descriptions of the sisters' actions regarding the粟米田 can be made more vivid.
*   The final sentence can be slightly adjusted for a more natural concluding tone.
```

