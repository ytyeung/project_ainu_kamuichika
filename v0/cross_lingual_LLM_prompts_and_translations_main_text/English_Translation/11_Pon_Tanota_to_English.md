# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Pon Okikirmui yaieyukar, “Tanota hurehure” 小オキキリムイが自ら歌った謡「この砂赤い赤い」

## This is translated from Chinese translation.

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
Translate the following text from Chinese to English. The original text is translation from Japanese which is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
Use story-telling and poetic tone. Keep the original meaning. Use modern and simple English.
If a term cannot be translated, keep the original language.

小オキキリムイ親自吟唱的歌謠
「這砂，紅豔豔的」

〔這砂，紅豔豔的〕
某日，我溯流而上，前去遊玩，
遇見了惡魔之子。
惡魔之子總是那般俊美，
容貌秀麗。身著黑色衣裳，
手持胡桃木的小弓，胡桃木的小箭。
他看見我，笑嘻嘻地說：
「小オキキリムイ，來玩吧！
我這就讓你看看，如何斷絕魚的生路。」
說著，他將胡桃木的小弓搭上胡桃木的小箭，
朝水源方向射去。
水源湧出胡桃木色的水，混濁不堪，
鮭魚們溯游而上，
卻因厭惡胡桃木水，哭泣著
退回下游。惡魔之子
見此情景，只是得意地笑。
我見狀，怒火中燒，
便拿出我的銀製小弓，搭上銀製小箭，
朝水源射去。
水源湧出銀色的水，清澈甘甜，
哭泣著離去的鮭魚們
在清澈的水中恢復了活力，
歡笑著，嬉鬧著，
啪嚓啪嚓地逆流而上。
惡魔之子頓時
面露他那與生俱來的怒容，
「你若真要如此，我就讓你看看，如何斷絕鹿的生路！」
說著，他將胡桃木的小弓搭上胡桃木的小箭，
射向天空，
山林的樹木間，颳起了
胡桃木之風，龍捲風。
從山林的樹木間，雄鹿群各自一方，
雌鹿群又在另一方，被風吹向天空，
整整齊齊地排列著，升向天際。
惡魔之子見此，得意地笑著。
我見狀，怒不可遏，
便拿起銀製小弓，搭上銀製小箭，
朝著鹿群離去的方向射去。
從天上，吹落下銀色的風，清新的風，
雄鹿群各自一方，
雌鹿群又在另一方，
被吹回山林的樹木間。
惡魔之子頓時
面露他那與生俱來的怒容，
「狂妄之徒，你若
真要如此，我們就來比試力氣！」
說著，他脫下了上衣。
我也只剩一件薄衣，
與他扭打在一起。他也緊緊抱住我。
從那以後，我們互相壓制，互相角力，
但惡魔之子的力氣之大，
實在令我驚訝。然而，終於，在某一刻，
我使出腰部的力量，全身的力量，
將惡魔之子
扛到肩上，
將他狠狠摔在山岩上，
發出轟然巨響。殺死了他，將他踢入地獄之後，
四周一片寂靜。
事情結束後，我沿著河流返回，
只聽見河中鮭魚們的歡笑聲，
嬉戲聲，熱鬧地傳來，
啪嚓啪嚓地響著。山林的樹木間，
雄鹿們，雌鹿們的歡笑聲，
嬉戲聲，充滿四處，
牠們在那裡，在這裡，
吃著東西。我見此情景，
感到安心，便回到
我的家。
小オキキリムイ如此講述著。
```

### Output
```
The Song of Little Okikirmui Himself:
"This sand, so red and vibrant."

(This sand, so red and vibrant)
One day, as I journeyed upstream for leisure,
I encountered the child of a demon.
Always so fair was this demon's child,
With a beautiful face. Clad in garments of black,
Holding a small bow of walnut wood, and arrows to match.
He saw me and said with a grin:
"Little Okikirmui, come and play!
I'll show you how to cut off the fish's path."
So saying, he notched a walnut arrow to his walnut bow,
And shot it towards the source of the stream.
From the source flowed water the color of walnut, murky and foul,
The salmon, swimming upstream,
Averted by the walnut water, cried,
And retreated downstream. The demon's child,
Seeing this, merely laughed in triumph.
My anger flared at the sight,
And I took out my small silver bow, notched a silver arrow,
And shot it towards the source.
From the source flowed silver water, clear and sweet,
The salmon, who had wept as they left,
Regained their vigor in the clear water,
Laughing and playing,
Splashing and frolicking upstream.
The demon's child then
Revealed his innate fury,
"If you insist, I'll show you how to cut off the deer's path!"
Saying this, he notched a walnut arrow to his walnut bow,
And shot it towards the sky,
Through the trees of the mountain forests blew
A walnut wind, a whirlwind.
From the trees of the mountain forests, the stags on one side,
The does on the other, were blown into the sky,
Neatly arranged, ascending to the heavens.
The demon's child, seeing this, laughed in triumph.
My rage knew no bounds,
And I took up my silver bow, notched a silver arrow,
And shot it towards the departing deer.
From the sky fell a silver wind, a refreshing wind,
The stags on one side,
The does on the other,
Were blown back to the trees of the mountain forests.
The demon's child then
Revealed his innate fury,
"Arrogant fool, if you
Insist on this, let us test our strength!"
Saying this, he removed his upper garment.
I, too, was left in but a thin robe,
And grappled with him. He held me tight.
From then on, we wrestled and struggled,
But the demon child's strength,
Truly astonished me. Yet, finally, at one moment,
I used the strength of my waist, the strength of my whole body,
And lifted the demon's child
Onto my shoulders,
Slamming him hard against the mountain rocks,
With a thunderous crash. Having killed him, and kicked him into hell,
All around was silent.
When it was over, I returned along the river,
And heard only the laughter of the salmon in the river,
The sounds of their play, resounding merrily,
Splashing and frolicking. Through the trees of the mountain forests,
The laughter of the stags and does,
The sounds of their play, filled the air,
They were there, they were here,
Eating their fill. Seeing this,
I felt at peace, and returned to
My home.
Little Okikirmui tells it so.
```
