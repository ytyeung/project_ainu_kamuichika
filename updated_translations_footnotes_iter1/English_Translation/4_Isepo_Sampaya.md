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
You are translating the following Japanese text into English. The original text is footnote. You already have a Chinese translation and an English translation.

Here are your tasks:

1. Criticise the English translation based on the Japanese text. 
2. Compare the Chinese translation with the English translation.
3. Improve the English translation, especially incoporating the pros of the Chinese translation.

Keep the original meanings. For the text which are not in Japanese, keep the original form.

This is the Japanese text.
(1) アマツポ(弩いしゆみ)すなわち「仕掛け弓」を仕掛ける事.
(2) 刀剣.これは戦争の時に使う刀剣とは違うので,ふだん家の右座の宝物の積んである上に吊してあるのがそれです.戦争の時には使いませんが,uniwente などのときには使います.

This is the Chinese translation.
(1)アマツポ(弩いしゆみ)，即是設置「詭計弓」。
(2)刀劍。這與戰爭時使用的刀劍不同，平時懸掛在家中右側堆放寶物之處。戰爭時不會使用，但在 *uniwente* 等場合會使用。

This is the English translation.
(1) Amatsupo (弩いしゆみ): That is, setting up a "trick bow."
(2) Swords. These are different from the swords used in war. They are usually hung above the pile of treasures on the right side of the house. They are not used in war, but are used during *uniwente*, etc.


```

### Output
```
(1) Amatsupo (弩いしゆみ): That is, setting up a "contrivance bow."
(2) Swords. These are different from swords used in war and are usually hung on the right side of the house where treasures are piled. They are not used in war but are used during *uniwente*, etc.

The English translation is generally accurate but could be improved by incorporating the conciseness and clarity of the Chinese translation, especially regarding the description of the swords' placement. The Chinese translation uses "詭計弓" which is more descriptive than "trick bow". The Chinese translation also more concisely describes where the swords are hung. The phrase "right side of the house where treasures are piled" is more direct than "above the pile of treasures on the right side of the house."
```

