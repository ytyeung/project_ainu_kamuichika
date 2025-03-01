# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Pipa yaieyukar, “Tonupeka ranran” 沼貝が自ら歌った謡「トヌペカ ランラン」

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

### Output
```
田螺之歌：Tonupeka Ranran

Tonupeka ranran,
烈日當空，我的家園乾涸,
我感覺自己快要 умирать 了。
「求求誰來給我們水，
請幫助我們！水，水！」我們哭喊著。
然後，從岸邊走來一位女子，
背上背著一個籃子。
我們哭泣著，她從我們身邊經過，
看到我們，她說，
「奇怪的田螺，可憐的田螺，你們為何哭泣，
發出如此嘈雜的聲音？ 」
她踐踏我們，把我們踢到一邊，
用我們的殼壓碎我們，
然後走進了深山。
「哦，好痛，好痛苦，水，水！」我們哭喊著。
然後，從岸邊又走來一位女子，
背上背著一個籃子。我們哭喊著，
「求求誰來給我們水，幫助我們！
哦，好痛，哦，好痛苦，水，水！」
然後，這位少女，帶著神聖而高貴的氣息，
來到我身邊，看到我們，她說，
「哦，你們這些可憐的東西，天氣真熱，田螺的
床都乾涸了，它們渴望著水。
發生了什麼事？看起來你們好像被踐踏過……」
她說著，把我們都撿了起來，
放在蜂斗菜的葉子上，
然後把我們放進了一個清澈的湖裡。
有了這純淨、冰冷的水，我們完全恢復了，
變得非常強壯。然後，我第一次，
調查了這些女子的本性。
第一個來，壓碎我的，可恨的女人，
這個邪惡的女人，是 Samayunkur 的
妹妹。可憐我們，
幫助我們的年輕少女，溫柔而優雅的那位，
是 Okikirmuy 的妹妹。
Samayunkur 的妹妹邪惡而可恨，
所以她的小米田枯萎了。Okikirmuy 的
妹妹的小米田，卻長勢茂盛。
那一年，Okikirmuy 的妹妹收穫了豐收。
她知道這是因為我，
所以她用田螺殼收割小米穗。
從那以後，每年，人類的女子
在收割小米穗時都會使用田螺殼。
於是，一隻田螺講述了這個故事。
```
