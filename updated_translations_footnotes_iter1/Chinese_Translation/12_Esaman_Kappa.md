# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

## Esaman yaieyukar, “Kappa reureu kappa” 獺かわうそが自ら歌った謡「カッパ レウレウ カッパ」

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
(1) achikara......「きたない」.おかしい,生意気なという意味をふくむ.
この物語は Okikirmui の父と pon nitnekamui の父とは,前に大層激しい戦争をしたことがあるので,この pon okikirmui と pon nitnekamui とは敵どうしになっています.その親たちの戦争した模様は別な物語に詳しく出ています.

This is the Chinese translation.
(1) achikara......意指「骯髒」。帶有奇怪、自大的意味。
這個故事中,Okikirmui 的父親和 pon nitnekamui 的父親之前曾爆發過非常激烈的戰爭,因此 pon okikirmui 和 pon nitnekamui 之間是敵對關係。關於他們父輩戰爭的詳細情況,在另一個故事中有詳細描述。


This is the English translation.
(1) achikara...... "kitanai" [dirty]. Includes meanings such as strange, impertinent.

In this story, the father of Okikirmui and the father of pon nitnekamui had a very fierce war in the past, so this pon okikirmui and pon nitnekamui are enemies. The details of the war between their parents are described in detail in another story.


```

### Output
```
(1) achikara......意指「骯髒」(kitanai)。帶有奇怪、傲慢的意味。

在這個故事中，Okikirmui 的父親和 pon nitnekamui 的父親之前曾爆發過非常激烈的戰爭，因此 pon okikirmui 和 pon nitnekamui 之間是敵對關係。關於他們父輩戰爭的詳細情況，在另一個故事中有詳細描述。

The Chinese translation is generally accurate but could be improved by incorporating some of the clarity and detail present in the English translation. Specifically, the English translation includes the original Japanese word "kitanai" and its direct translation "dirty", which provides additional context. The Chinese translation could benefit from including the romanized Japanese word for clarity. Also, the English translation uses 'impertinent' which is more precise than '自大'.
```

