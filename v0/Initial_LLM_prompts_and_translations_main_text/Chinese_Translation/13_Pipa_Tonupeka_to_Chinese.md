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
Translate the following text from Japanese to Chinese. The original text is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original Japanese meaning accurately. Use modern Chinese. Display in Traditional Chinese.
If a term cannot be translated, keep the original language.

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
沼貝親自吟唱的歌謠「托努佩卡 蘭蘭」

托努佩卡 蘭蘭
強烈的日光將我棲身之所
曬得乾涸，我奄奄一息，瀕臨死亡。
「誰能慈悲，賜予我等甘霖，
拯救我等性命？水啊，水啊！」我等哀嚎哭泣。
遠遠地，從海濱方向走來一位女子，
背負著竹簍。
我等哭泣著，她從我等身旁經過，
看見我等，便說道：
「可憎的沼貝，惡劣的沼貝，為何哭泣，
喧鬧不休，擾人清靜！」
說罷，她便踐踏我等，用腳尖踢打，將我等連同貝殼一同碾碎，
揚長而去，徑直走向山林深處。
「啊，痛楚難忍，苦不堪言，水啊，水啊！」我等哀嚎哭泣。
遠遠地，從海濱方向又走來一位女子，
背負著竹簍。我等呼喊：
「但願有人能賜予我等甘霖，拯救我等性命，
啊，痛楚難忍，苦不堪言，水啊，水啊！」
那女子，宛如神祇般美麗高貴，
來到我等身旁，看見我等，便說道：
「啊，多麼可憐，天氣如此炎熱，沼貝們的
居所也已乾涸，渴望著甘霖，
究竟發生了什麼事呢？
似乎是被踐踏過了……」
說著，她便將我等一一拾起，
放入蕗葉之中，再將我等放入清澈的湖水之中。
清澈冰涼的湖水使我等徹底恢復了元氣，
變得無比強壯。於是，我等開始探尋
她們的性情。
原來，先前到來，將我等踐踏的
可憎女子，邪惡女子，是薩瑪雲庫爾的
妹妹；而憐憫我等，
拯救我等的年輕女子，溫柔嫻靜的女子，
則是奧基基里穆伊的妹妹。
薩瑪雲庫爾的妹妹心懷惡意，
使她的粟米田枯萎凋零；而奧基基里穆伊的
妹妹，則使她的粟米田豐收富饒。
那一年，奧基基里穆伊的妹妹收穫了大量的粟米。
她知曉這是因為我的緣故，
便用沼貝的貝殼來摘取粟米的穗。
從此以後，每年，人類的女子們
在摘取粟米穗時，都會使用沼貝的貝殼。
這，就是一隻沼貝所講述的故事。
```
