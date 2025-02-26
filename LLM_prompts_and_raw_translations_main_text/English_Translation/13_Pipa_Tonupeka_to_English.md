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
Translate the following text from Japanese to English. The original text is a poem. Try to make the translation poetic but keep the original meanings.

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
Here's a translation of the poem, aiming for a balance between accuracy and poetic feel:

**The Swamp Snail's Song: "Tonupeka Ranran"**

Tonupeka ranran,
Under the sun's fierce glare, my home is parched,
Death feels so near, my life almost departs.
"Oh, someone, grant us water, let us drink,
Save us, we pray! Water, water!" we shriek.
Then, from the shore, a woman comes in sight,
A basket on her back, approaching in the light.
We weep and wail, but she just passes by,
Glances down at us with a scornful eye.

"Foolish swamp snails, wretched, whining things,
Why do you cry, what clamor do you bring?"
She scorns, and crushes us beneath her heel,
Scatters our shells, her heart devoid of feel,
Then strides away, towards the mountains high.
"Oh, pain, oh, suffering, water!" we cry.

Again, from the shore, a woman draws near,
A basket on her back, dispelling all fear.
We plead, "Oh, someone, grant us water, we implore,
Save us from pain, from suffering evermore!
Water, water!" we cry, our voices weak.
Then, like a goddess, gentle and meek,
A maiden approaches, with grace so divine,
Looks down at us, her eyes with pity shine.

"Ah, poor creatures, suffering in this heat,
Your beds are dry, water you crave to meet.
What has befallen you? It seems you've been trod..."
She gathers us gently, blessed by God,
Places us softly on broad butterbur leaves,
And carries us gently where the clear lake weaves.

In pure, cool water, our strength is restored,
Our spirits revived, our health adored.
Then, we discern the nature of these two,
The cruel one who crushed us, her heart askew,
Was Samayunkur's sister, filled with spite,
While the kind maiden, bathed in gentle light,
Who rescued us, so tender and so fair,
Was Okikirimui's sister, beyond compare.

Samayunkur's sister, with her wicked ways,
Caused her millet fields to wither in the haze,
But Okikirimui's sister, with her gentle hand,
Made her millet fields flourish across the land.
That year, Okikirimui's sister reaped a harvest grand.
Knowing my part in this, across the sand,
She used swamp snail shells to harvest every strand.

And since that day, the women of the land,
When harvesting millet, with swamp snail shells in hand,
Remember the snails, and the tale they understand.
Thus, spoke the swamp snail, from the water's edge.

```
### Another prompt for matched meaning

```
Translate the following text from Japanese to English. Keep the original meanings.
```

### Output of this prompt

```
Here's an English translation of the Japanese text, aiming to preserve the original meaning and tone:

**The Pond Snail's Own Sung Song: "Tonupeka Ranran"**

Tonupeka Ranran
The intense sunlight has dried up the place where I am,
and I feel like I'm about to die.
"If only someone would give us water to drink
and help us. Water, water!" we cry out.
Then, from far off on the beach, a woman
comes carrying a basket on her back.
As we cry, she passes by us,
and when she sees us, she says,
"Silly pond snails, bad pond snails, what are you crying about,
making such a noisy fuss?" And she
tramples on us, kicks us away, crushing us with our shells,
and goes off towards the mountains.
"Oh, it hurts, it's painful, water, water!" we cry out.
Then, from far off on the beach, another woman
comes carrying a basket on her back. We
cried out, "If only someone would give us water to drink and help us,
Oh, it hurts, oh, it's painful, water, water!"
Then, the young woman, with a divine, beautiful, and noble air,
came to our side, and when she saw us, she said,
"Oh, how pitiful, it's so hot, and the pond snails'
beds have dried up, and they're longing for water.
What happened? It looks like they've been trampled on..."
As she said this, she gathered us all up
and put us in butterbur leaves,
and placed us in a beautiful lake.
We completely recovered our strength with the pure, cold water,
and became very healthy. Then, for the first time,
we investigated the nature of those women.
It turned out that the hateful woman who came first
and trampled on me, the bad woman, was Samayunkuru's
younger sister, and the young woman who pitied us
and helped us, the gentle and graceful one,
was Okikirmui's younger sister.
Samayunkuru's sister was wicked and hateful, so
she caused her millet field to wither, and Okikirmui's
sister caused her millet field to bear much fruit.
That year, Okikirmui's sister harvested a great amount.
Knowing that it was because of me,
she picked the millet ears with pond snail shells.
Since then, every year, human women
have used pond snail shells when picking millet ears.
So, one pond snail narrated.

```