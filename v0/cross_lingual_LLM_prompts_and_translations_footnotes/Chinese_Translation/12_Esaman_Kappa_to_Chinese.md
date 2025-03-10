# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Esaman yaieyukar, “Kappa reureu kappa” 獺かわうそが自ら歌った謡「カッパ レウレウ カッパ」

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

(1) achikara...... "kitanai" [dirty]. Includes meanings such as strange, impertinent.

In this story, the father of Okikirmui and the father of pon nitnekamui had a very fierce war in the past, so this pon okikirmui and pon nitnekamui are enemies. The details of the war between their parents are described in detail in another story.

```

### Output
```
(1) achikara...... "kitanai" [dirty/骯髒]. 包含奇怪、冒昧等含義。

在這個故事中，Okikirmui 的父親和 pon nitnekamui 的父親過去曾發生過非常激烈的戰爭，所以這個 pon okikirmui 和 pon nitnekamui 是敵人。他們父母之間戰爭的細節在另一個故事中有詳細描述。
```
