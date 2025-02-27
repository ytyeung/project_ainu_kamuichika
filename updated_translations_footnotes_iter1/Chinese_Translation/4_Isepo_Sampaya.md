# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

## Isepo yaieyukar, “Sampaya terke” 兎が自ら歌った謡「サンパヤ テレケ」

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
You are translating the following Japanese text into Chinese. The original text is footnote. You already have a Chinese translation and an English translation.

Here are your tasks:

1. Criticise the Chinese translation based on the Japanese text. 
2. Compare the Chinese translation with the English translation.
3. Improve the Chinese translation, especially incoporating the pros of the English translation.

Keep the original meanings. For the text which are not in Japanese, keep the original form. Display in Traditional Chinese.

This is the Japanese text.
(1) アマツポ(弩いしゆみ)すなわち「仕掛け弓」を仕掛ける事.
(2) 刀剣.これは戦争の時に使う刀剣とは違うので,ふだん家の右座の宝物の積んである上に吊してあるのがそれです.戦争の時には使いませんが,uniwente などのときには使います.

This is the Chinese translation.
(1) アマツポ(弩いしゆみ),即「機關弓」的設置。
(2) 刀劍。此與戰爭時使用的刀劍不同,平時是吊在家中右座堆放寶物之處。戰爭時不會使用,但在 uniwente 等場合會使用。


This is the English translation.
(1) Amatsupo (弩いしゆみ): That is, setting up a "trick bow."
(2) Swords. These are different from the swords used in war. They are usually hung above the pile of treasures on the right side of the house. They are not used in war, but are used during *uniwente*, etc.


```

### Output
```
(1)アマツポ(弩いしゆみ)，即是設置「詭計弓」。
(2)刀劍。這與戰爭時使用的刀劍不同，平時懸掛在家中右側堆放寶物之處。戰爭時不會使用，但在 *uniwente* 等場合會使用。

The Chinese translation is generally accurate but lacks some of the nuance present in the Japanese and English versions. For (1), "機關弓的設置" is a bit too literal and doesn't quite capture the sense of 'setting up a trick'. For (2), the Chinese translation is adequate, but could benefit from a slightly more descriptive tone, similar to the English version. The English translation provides a clearer explanation of the context and purpose of the items described. It also correctly italicizes *uniwente*. The updated translation aims to incorporate these improvements.
```

