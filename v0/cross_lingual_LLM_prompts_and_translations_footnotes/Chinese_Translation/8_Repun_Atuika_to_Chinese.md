# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Repun Kamui yaieyukar, “Atuika tomatomaki kuntuteashi hm hm!” 海の神が自ら歌った謡「アトイカ トマトマキ クントテアシ フム フム!」

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

(1) This is an ornament decorated with *gohei* (paper streamers), and it is used when offering sake to the gods. This *kike-ush-pashui* acts as a representative of humans, and it is said to go to the gods and convey what humans want to say to them. Ordinary chopsticks without *gohei* are called *iku pashui* (chopsticks for feasts).

```

### Output
```
這是一種用*gohei*（紙垂）裝飾的飾品，用於向神靈供奉清酒。這種*kike-ush-pashui*作為人類的代表，據說會去到神靈那裡，並傳達人類想對他們說的話。沒有*gohei*的普通筷子被稱為*iku pashui*（宴會用筷子）。
```
