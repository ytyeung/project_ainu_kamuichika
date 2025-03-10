# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of

## Esaman yaieyukar, “Kappa reureu kappa” 獺かわうそが自ら歌った謡「カッパ レウレウ カッパ」

## This is translated from Chinese translation.

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
Translate the following text from Chinese to English. The original text is translation from Japanese which is a footnotes of Ainu chants. 
Keep the original meaning. Use modern and simple English.
If a term cannot be translated, keep the original language.

(1) achikara......意指「骯髒」。帶有奇怪、自大的意味。
這個故事中,Okikirmui 的父親和 pon nitnekamui 的父親之前曾爆發過非常激烈的戰爭,因此 pon okikirmui 和 pon nitnekamui 之間是敵對關係。關於他們父輩戰爭的詳細情況,在另一個故事中有詳細描述。

```

### Output
```
(1) achikara......means "dirty." It carries a sense of strangeness and arrogance.
In this story, Okikirmui's father and pon nitnekamui's father had a very fierce war before, so pon okikirmui and pon nitnekamui are in a hostile relationship. The details of their fathers' war are described in detail in another story.
```
