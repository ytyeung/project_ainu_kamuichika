# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Pon Okikirmui yaieyukar, “Tanota hurehure” 小オキキリムイが自ら歌った謡「この砂赤い赤い」

## This is translated from English translation.

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
Translate the following text from English to Chinese. The original text is translation from Japanese which is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original meaning. Use modern Chinese. Display in Traditional Chinese. Only allow Chinese and English characters.
If a term cannot be translated, keep the original language.

A song sung by Little Okikirmui himself:
"This sand, red, so red."

This sand, red, so red,
One day, venturing upstream for play,
I encountered a child of the devil.
Always, the devil's child possessed a beautiful air,
A beautiful face, adorned in black robes,
A small bow of walnut, with arrows of walnut he held.
Seeing me, he grinned,
saying,
"Little Okikirmui, let us play.
Now, I shall show you how to cut off the fish's roots."
So saying, with his walnut bow and walnut arrow,
He aimed and shot towards the water source.
From the source, walnut water, turbid water flowed,
And the salmon, as they tried to ascend,
Loathing the walnut water, cried and retreated with the flow.
The devil's child, he grinned at this.
Seeing this, I was angered,
And with my silver bow and silver arrow,
I aimed and shot towards the water source.
From the source, silver water, pure water flowed,
And the salmon, who had cried as they retreated,
Regained their vigor in the pure water,
Laughing and frolicking,
Splashing and ascending the river.
Then, the devil's child,
His inherent temper showing on his face,
said,
"If you truly do such a thing, I shall show you how to cut off the deer's roots."
And saying so, with his walnut bow and walnut arrow,
He shot into the vast sky.
From the mountain's fields,
Walnut wind, a whirlwind, blew forth,
And from the mountain's fields,
The stags in one group,
The does in another,
Were blown upwards by the wind,
Ascending neatly into the sky.
The devil's child, he grinned.
Seeing this, I was enraged,
And with my silver bow and silver arrow,
I aimed and shot after the deer.
From the heavens,
Silver wind, pure wind, blew down,
The stags in one group,
The does in another,
Were blown down upon the mountain's fields.
Then, the devil's child,
His inherent temper showing on his face,
said,
"Insolent one, if you truly
do such a thing, let us have a contest of strength."
And saying so, he removed his outer garment.
I, too, in a thin robe,
Grappled with him. He grappled with me. From then on,
We wrestled, sometimes below, sometimes above,
But I was astonished by the devil's child's great strength.
Yet, finally, at a certain moment,
I gathered all the strength in my waist, in my body,
And lifted the devil's child
Up to my shoulders,
And the sound of me slamming him upon the mountain rocks
Resounded with a clang. After killing him and
kicking him down to hell, all became silent.
That done, as I returned along the stream,
From within the river, the voices of salmon laughing,
The sounds of play, rose clamorously,
Splashing and echoing. In the mountain's fields,
The voices of stags and does laughing,
The sounds of play, filled the air,
Eating here and there. Seeing this, I was relieved,
And returned to my home.
So, Little Okikirmui told his story.
```

### Output
```
小Okikirmui 吟唱之歌：
「這沙，紅啊，真紅。」

這沙，紅啊，真紅，
一日，我溯溪嬉戲，
竟遇見了魔神之子。
魔神之子，總帶著一股妖冶之氣，
俊美的臉龐，身著一襲黑袍，
手持小小的胡桃木弓，胡桃木箭。
他見到我，咧嘴一笑，
說道：
「小Okikirmui，我們來玩耍吧。
現在，我就讓你見識見識，如何斬斷魚的命脈。」
說罷，他便以胡桃木弓，胡桃木箭，
瞄準水源射去。
源頭湧出胡桃木之水，混濁不堪，
鮭魚們奮力上溯，
厭惡那胡桃木之水，哀號著退回下游。
魔神之子，見此情景，得意地笑了。
我見狀，怒火中燒，
便以我的銀弓，銀箭，
瞄準水源射去。
源頭湧出銀色之水，清澈甘甜，
鮭魚們方才哀號退卻，
如今在這清澈之水中重獲生機，
歡笑嬉戲，
潑灑著水花，逆流而上。
魔神之子，
本性畢露，怒形於色，
說道：
「你若真要如此，我就讓你見識見識，如何斬斷鹿的命脈。」
說罷，他便以胡桃木弓，胡桃木箭，
射向遼闊的天空。
自山野之間，
胡桃木之風，旋風般呼嘯而起，
自山野之間，
雄鹿成群，
雌鹿成隊，
被狂風捲起，
整整齊齊地升入天空。
魔神之子，得意地笑了。
我見狀，怒不可遏，
便以我的銀弓，銀箭，
瞄準鹿群射去。
自天而降，
銀色之風，清冽之風，吹拂而下，
雄鹿成群，
雌鹿成隊，
被吹回山野之間。
魔神之子，
本性畢露，怒形於色，
說道：
「狂妄之徒，你若真要
如此，我們就來比試比試力氣。」
說罷，他便脫去外袍。
我亦身著單薄衣衫，
與他扭打在一起。他與我互相角力。自此，
我們時而 নিচে，時而 উপরে，
但我驚訝於魔神之子力大無窮。
然，終在某一刻，
我凝聚腰間，全身之力，
將魔神之子舉起，
高過我的肩膀，
將他狠狠摔在山岩之上，
那聲巨響，震耳欲聾。殺死他後，
將他踢入地獄，一切歸於寂靜。
事畢，我沿溪而返，
自河川之中，鮭魚們的歡笑聲，
嬉戲之聲，喧囂而起，
潑灑迴盪。在山野之間，
雄鹿與雌鹿的歡笑聲，
嬉戲之聲，盈滿天地，
四處覓食。見此情景，我如釋重負，
返回我的家園。
這便是，小Okikirmui 所述的故事。
```
