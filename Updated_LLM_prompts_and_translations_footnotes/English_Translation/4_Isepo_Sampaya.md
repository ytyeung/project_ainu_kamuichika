# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated English Translation of

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
You are a professional translator. You know Japanese, English and Chinese. You can translate Japanese into either Chinese or English. You can also translation Chinese into English, and English into Chinese.

```

### Prompt
```
You are translating the following Japanese text into English. The original text is a Japanese translation of footnotes a Ainu chant. 
You have 2 versions of English translations at hand.

Here are your tasks:

1. Compare the two English translations with the original Japanese text. List out the Pros and Cons of the two Translations.
2. Choose a better translation. Accuracy of meaning is the most important criterion. Easy to understand is the second.
3. Based on the better translation, translate the Japanese text into English again, incorporating the Pros of the two translations.

Keep the original Japanese meaning accurately. Use modern and simple English for easy understanding. 
If a term cannot be translated, keep the original language.
For the text which are not in Japanese, keep the original form. 

This is the Japanese text.
(1) アマツポ(弩いしゆみ)すなわち「仕掛け弓」を仕掛ける事.
(2) 刀剣.これは戦争の時に使う刀剣とは違うので,ふだん家の右座の宝物の積んである上に吊してあるのがそれです.戦争の時には使いませんが,uniwente などのときには使います.

This is the English Translation 1.
(1) Amatsupo (弩いしゆみ): That is, setting up a "trick bow."
(2) Swords. These are different from the swords used in war. They are usually hung above the pile of treasures on the right side of the house. They are not used in war, but are used during *uniwente*, etc.


This is the English Translation 2.
(1) Amatupo (弩いしゆみ), which is the installation of "mechanism bow". (2) Swords. These are different from the swords used in war. Usually, they are hung at the right seat where treasures are piled up at home. They are not used in war, but they are used in occasions such as uniwente.

```

### Output
```
(1) Amatupo (弩いしゆみ): This refers to setting up a "trick bow" (mechanism bow).
(2) Swords. These are different from the swords used in war. They are usually hung above the pile of treasures on the right side of the house. They are not used in war, but are used during occasions such as *uniwente*.

Analysis of the two translations:

Translation 1:
Pros: Simple and direct. Uses the term "trick bow" which is easily understandable.
Cons: Less descriptive, doesn't fully explain the context of the swords.

Translation 2:
Pros: More descriptive, providing more context about where the swords are kept. "Mechanism bow" is a more literal translation.
Cons: Slightly less fluent than Translation 1. "Mechanism bow" is less common than "trick bow".

Choice of Better Translation: Translation 2 is slightly better due to its greater accuracy and detail.

Improvements: Combining the strengths of both translations, using "trick bow" for clarity and incorporating the descriptive details from Translation 2.
```

