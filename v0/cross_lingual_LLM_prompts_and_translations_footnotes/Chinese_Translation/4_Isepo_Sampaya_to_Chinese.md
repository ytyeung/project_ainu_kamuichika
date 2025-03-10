# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Chinese Translation of

## Isepo yaieyukar, “Sampaya terke” 兎が自ら歌った謡「サンパヤ テレケ」

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

(1) Amatsupo (弩いしゆみ): That is, setting up a "trick bow."
(2) Swords. These are different from the swords used in war. They are usually hung above the pile of treasures on the right side of the house. They are not used in war, but are used during *uniwente*, etc.

```

### Output
```
（1）Amatsupo (弩いしゆみ)：意即設置一個「機關弓」。
（2）劍。這些與戰爭中使用的劍不同。它們通常懸掛在房屋右側的寶物堆之上。它們不用於戰爭，而是用於 *uniwente* 等場合。
```
