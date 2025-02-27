# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

## Pon Horkeukamui yaieyukar, “Hotenao” 小狼の神が自ら歌った謡「ホテナオ」

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


This is the Chinese translation.
需要日文原文、中文翻譯和英文翻譯才能進行翻譯更新。

This is the English translation.
There are no numbered items in the provided text.


```

### Output
```
The Japanese original, Chinese translation, and English translation are required to perform translation updates.

The English translation is completely off. The Japanese text indicates that the original text, Chinese translation, and English translation are all needed for translation updates. The original English translation incorrectly states that there are no numbered items. The Chinese translation accurately reflects the meaning of the Japanese text. The improved English translation should be aligned with the Japanese and Chinese.
```

