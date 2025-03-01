# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## English Translation of Chiri's footnotes on

## Repun Kamui yaieyukar, “Atuika tomatomaki kuntuteashi hm hm!” 海の神が自ら歌った謡「アトイカ トマトマキ クントテアシ フム フム!」

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
Translate the following text from Japanese to English. The original text is footnote. Keep the original meanings. For the text which are not in Japanese, keep the original form.

(1) 御幣で飾りをつけたものであって,神様にお神酒を上げる時に使います.この kike-ush-pashui は人間の代理を勤めて,人間が神様に云おうと思う事を神様のところへ行って,伝えると云います.御幣をつけていない普通の箸を iku pashui と云います(酒宴の箸).
```

### Output
```
(1) This is an ornament decorated with *gohei* (paper streamers), and it is used when offering sake to the gods. This *kike-ush-pashui* acts as a representative of humans, and it is said to go to the gods and convey what humans want to say to them. Ordinary chopsticks without *gohei* are called *iku pashui* (chopsticks for feasts).

```