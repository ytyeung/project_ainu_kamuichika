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
(1) katken......川ガラス.昔から大そういい鳥として尊ばれる鳥です.

This is the Chinese translation.
(1) katken......河烏。自古以來就被視為非常好的鳥，備受尊崇。

This is the English translation.
(1) katken......River Dipper. It is a bird that has been highly respected as a very good bird since ancient times.


```

### Output
```
(1) katken......River Dipper. It is a bird highly revered since ancient times for its excellence.

The English translation is a bit repetitive, especially with "very good bird". The Chinese translation is more concise and elegant. The phrase "備受尊崇" (bèi shòu zūn chóng) captures the nuance of being highly respected in a more sophisticated way than "highly respected as a very good bird". The updated translation will aim for conciseness and elegance, incorporating the spirit of the Chinese translation.
```

