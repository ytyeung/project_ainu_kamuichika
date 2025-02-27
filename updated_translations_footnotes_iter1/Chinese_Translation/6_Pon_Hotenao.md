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
You are translating the following Japanese text into Chinese. The original text is footnote. You already have a Chinese translation and an English translation.

Here are your tasks:

1. Criticise the Chinese translation based on the Japanese text. 
2. Compare the Chinese translation with the English translation.
3. Improve the Chinese translation, especially incoporating the pros of the English translation.

Keep the original meanings. For the text which are not in Japanese, keep the original form. Display in Traditional Chinese.

This is the Japanese text.


This is the Chinese translation.
There are no numbered items in the provided text.


This is the English translation.
There are no numbered items in the provided text.


```

### Output
```
需要日文原文、中文翻譯和英文翻譯才能進行翻譯更新。

Since there is no text provided, I cannot fulfill the user's request. Please provide the Japanese text, the Chinese translation, and the English translation to proceed.
```

