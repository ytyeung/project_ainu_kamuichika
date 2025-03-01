# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Terkepi yaieyukar, “Tororo hanrok hanrok!” 蛙が自らを歌った謡「トーロロ ハンロク ハンロク!」

## This is translated from English translation.

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
Translate the following text from English to Chinese. The original text is translation from Japanese which is footnotes of Ainu chant. 
Keep the original meaning. Use modern Chinese. Display in Traditional Chinese. Only allow Chinese and English characters.
If a term cannot be translated, keep the original language.

There are no numbered items in the provided text.

```

### Output
```
請提供需要翻譯的英文文本（源自日文，是阿伊努語吟唱的腳註）。我會將其翻譯成繁體中文，保持原文含義，並使用現代中文。無法翻譯的術語將保留原始語言。
```
