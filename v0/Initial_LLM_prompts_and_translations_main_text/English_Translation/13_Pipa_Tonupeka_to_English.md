# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

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
Translate the following text from Japanese to English. The original text is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original Japanese meaning accurately. Use modern and simple English.
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
The Pond Snail's Own Song: "Tonupeka Ranran"

Tonupeka ranran,
Under the fierce sunlight, my home dries,
I feel as if I'm about to die.
"Someone, please give us water,
please help us! Water, water!" we cried.
Then, from the shore, a woman came,
a basket upon her back.
As we wept, she passed by us,
and seeing us, she said,
"Strange pond snails, wretched pond snails, why do you cry
and make such a noisy fuss?"
She trampled us, kicked us aside,
crushing us with our shells,
then went far into the mountains.
"Oh, it hurts, it's painful, water, water!" we cried.
Then, from the shore, another woman came,
a basket upon her back. We cried,
"Someone, please give us water and help us!
Oh, it hurts, oh, it's painful, water, water!"
Then, the maiden, with a divine and noble air,
came to my side and seeing us, she said,
"Oh, you poor things, it's so hot, the pond snails'
beds have dried up, and they thirst for water.
What has happened? It looks as if you've been trampled..."
As she spoke, she gathered us all up,
placed us on butterbur leaves,
and put us in a clear lake.
With the pure, cold water, we fully recovered,
and became very strong. Then, for the first time,
I investigated the nature of these women.
The hateful woman who came first and crushed me,
the wicked woman, was Samayunkur's
sister. The young maiden who pitied us
and helped us, the gentle and graceful one,
was Okikirmuy's sister.
Samayunkur's sister was evil and hateful,
so her millet field withered. Okikirmuy's
sister's millet field, however, flourished.
That year, Okikirmuy's sister harvested a great abundance.
Knowing it was because of me,
she harvested the millet ears with pond snail shells.
Since then, every year, human women
have used pond snail shells when harvesting millet ears.
So, a pond snail told the story.
```
