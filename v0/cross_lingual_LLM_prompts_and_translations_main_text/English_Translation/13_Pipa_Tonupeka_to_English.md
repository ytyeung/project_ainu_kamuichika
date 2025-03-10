# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Pipa yaieyukar, “Tonupeka ranran” 沼貝が自ら歌った謡「トヌペカ ランラン」

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

### Output
```
The Song of *Tonopeka Ranran*, sung by the clam itself:

*Tonopeka Ranran*
The fierce sun has parched my dwelling,
I am weak, nearing death.
"Who will have mercy, grant us rain,
Save our lives? Water, water!" we cry.
Far off, from the direction of the shore, a woman approaches,
Carrying a bamboo basket.
As we weep, she passes by,
Sees us, and says:
"Loathsome *numakai*, wretched *numakai*, why do you cry,
Making such a racket, disturbing the peace!"
Having said this, she tramples us, kicks us with her toes, crushing us along with our shells,
And strides away, heading straight into the depths of the mountains.
"Ah, the pain is unbearable, the suffering immense, water, water!" we cry.
Far off, from the direction of the shore, another woman approaches,
Carrying a bamboo basket. We call out:
"If only someone would grant us rain, save our lives,
Ah, the pain is unbearable, the suffering immense, water, water!"
That woman, as beautiful and noble as a goddess,
Comes to our side, sees us, and says:
"Ah, how pitiful, the weather is so hot, the *numakai*'s
dwelling has dried up, longing for rain,
What on earth has happened?
It seems they have been trampled…"
Saying this, she picks us up one by one,
Places us in *fuki* leaves, and then places us in the clear lake water.
The clear, cool lake water completely restores our vitality,
Making us incredibly strong. And so, we begin to investigate
their natures.
It turns out, the loathsome woman who came earlier and trampled us,
the wicked woman, is *Samaunkur*’s
sister; while the young woman who pitied us,
the gentle and quiet woman who saved us,
is *Okikirmui*’s sister.
*Samaunkur*’s sister harbors malice,
causing her millet fields to wither and die; while *Okikirmui*’s
sister causes her millet fields to be abundant and rich.
That year, *Okikirmui*’s sister harvested a large amount of millet.
She knew this was because of me,
So she used the shells of the *numakai* to pluck the ears of millet.
From then on, every year, the women of humankind
use the shells of the *numakai* when plucking the ears of millet.
This, is the story told by a single *numakai*.
```
