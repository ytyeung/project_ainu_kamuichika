# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

## Kamuichikap Kamui yaieyukar, “Konkuwa” 梟の神が自ら歌った謡「コンクワ」

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
You are translating the following Japanese text into Chinese. The original text is a Japanese translation of footnotes a Ainu chant. 
You have 2 versions of Chinese translations at hand.

Here are your tasks:

1. Compare the two Chinese translations with the original Japanese text. List out the Pros and Cons of the two Translations.
2. Choose a better translation. Accuracy of meaning is the most important criterion. Easy to understand is the second.
3. Based on the better translation, translate the Japanese text into Chinese again, incorporating the Pros of the two translations.

Keep the original Japanese meaning accurately. Use modern Chinese for easy understanding. Display in Traditional Chinese. 
If a term cannot be translated, keep the original language.
For the text which are not in Japanese, keep the original form. 

This is the Japanese text.
(1) katken......川ガラス.昔から大そういい鳥として尊ばれる鳥です.

This is the Chinese Translation 1.
(1) katken......川玻璃。自古以來就被視為非常吉祥的鳥。


This is the Chinese Translation 2.
katken......河烏。自古以來，牠是一種備受尊敬的鳥類，被視為非常吉祥的鳥。

```

### Output
```
katken......河烏。自古以來，牠是一種備受尊崇的鳥類。

Analysis of the two Chinese translations:

Translation 1:
Pros: More concise.
Cons: "川玻璃" is not a common or accurate translation for "川ガラス" (kawagarasu). It sounds unnatural.

Translation 2:
Pros: "河烏" is a more accurate and common translation for "川ガラス". More detailed and easier to understand.
Cons: Slightly verbose.

Choice of Better Translation:
Translation 2 is better because it prioritizes accuracy in translating "川ガラス".

Improved Translation Strategy:
Incorporate the conciseness of Translation 1 while maintaining the accuracy of Translation 2.
```

