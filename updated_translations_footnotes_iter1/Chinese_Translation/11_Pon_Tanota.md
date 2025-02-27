# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

## Pon Okikirmui yaieyukar, “Tanota hurehure” 小オキキリムイが自ら歌った謡「この砂赤い赤い」

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
(1) iwan poknashir......六つの地獄.地の下には六段の世界があってそこには種々な悪魔が住んでいます.

This is the Chinese translation.
(1) iwan poknashir......六個地獄。地底下有六層世界,那裡住著各式各樣的惡魔。


This is the English translation.
(1) iwan poknashir......Six Hells. Beneath the earth, there are six levels, and various demons dwell there.


```

### Output
```
(1) iwan poknashir......六個地獄。地底下有六層世界，那裡住著各式各樣的惡魔。

The original Chinese translation is generally accurate but can be improved by incorporating the clarity and flow of the English translation. Specifically, the phrase "種々な悪魔" can be made more descriptive. The English translation's use of "various demons" is a good model.
```

