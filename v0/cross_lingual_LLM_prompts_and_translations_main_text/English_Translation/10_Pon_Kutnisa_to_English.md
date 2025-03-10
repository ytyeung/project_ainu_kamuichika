# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Pon Okikirmui yaieyukar, “Kutnisa kutunkutun” 小オキキリムイが自ら歌った謡「クツニサ クトンクトン」

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
「クツニサ クトンクトン」

クツニサ クトンクトン
在某一天，我前往水源地遊玩，
發現水源邊有個小矮人，
正彎著腰，一下又一下地敲打著，
想用胡桃木搭建魚梁。
他看見了我，便說道：
「你是誰？我的姪子啊，幫我個忙吧。」
我仔細一看，那魚梁竟是用胡桃木做的，
胡桃木的汁液，混著混濁的水流淌而下，
鮭魚們想逆流而上，卻厭惡胡桃木的味道，
哭泣著，轉身離去。我頓時怒火中燒，
一把奪過小矮人手中敲打木樁的槌子，
朝著他的腰椎中央，
狠狠地敲了下去，發出「砰」的一聲巨響。
我將小矮人的腰椎打斷，殺死了他，
並將他踢入了地獄深淵。我試著搖晃他用胡桃木做的木樁，
似乎一直延伸到了第六層地獄的彼方。
於是，我用盡腰部的力量，全身的力氣，
將那木樁從根部徹底折斷，
也將它踢入了地獄之中。
水源恢復了清澈，清新的風，清澈的水，
流淌而下，那些原本哭泣著離去的
鮭魚們，在清風和清水的滋潤下，
恢復了活力，牠們歡欣鼓舞，嬉戲玩耍，
拍打著水花，奮力向上游去。
我看到這一幕，感到十分欣慰，
便沿著河流，踏上了歸途。這就是
小オキキリムイ所講述的故事。
```

### Output
```
A song sung by little Okikirmui himself:
"Kutnisa Kuton Kutton"

Kutnisa Kuton Kutton,
One day, as I wandered to the source of the waters,
I saw a little person by the water's edge,
Bent over, striking again and again,
Trying to build a fish weir of walnut wood.
He saw me and said:
"Who are you? Nephew, lend me a hand."
I looked closely, and the weir was indeed of walnut,
The sap of the walnut mixing with the muddy stream,
The salmon, wishing to swim upstream, hated the walnut's scent,
Weeping, they turned and fled. A fire ignited within me,
I snatched the mallet from the little person's hand,
And struck his spine,
Right in the center, a resounding "bang!"
I broke his spine, I killed him,
And kicked him into the abyss of hell. I tried to shake the walnut stakes he had made,
They seemed to stretch to the sixth level of hell and beyond.
Then, with all the strength in my waist, all the power in my body,
I snapped the stakes from their roots,
And kicked them into hell as well.
The water source became clear again, fresh wind, clear water,
Flowed down, and those who had wept and fled,
The salmon, nourished by the clear wind and water,
Regained their vigor, they rejoiced and played,
Splashing and struggling upstream.
Seeing this, I was filled with joy,
And I set out on the path home along the river. This is the story
told by little Okikirmui.
```
