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
You are a professional translator. You know Japanese, English and Chinese. You can translate Japanese into either Chinese or English. You can also translation Chinese into English, and English into Chinese.

```

### Prompt
```
You are translating the following Japanese text into Chinese. The original text is a Japanese translation of footnotes a Ainu chant. 
You have 2 versions of Chinese translations at hand.

Here are your tasks:

1. Compare the two Chinese translations with the original Japanese text. List out the Pros and Cons of the two Translations.
2. Choose a better translation. Accuracy of meaning is the most important criterion. Easy to understand is the second.
3. Based on the better translation, translate the Japanese text into Chinese again, incorporating the Pros of the two translations.

Keep the original Japanese meaning accurately. Use modern Chinese for easy understanding. Display in Traditional Chinese. 
If a term cannot be translated, keep the original language.
For the text which are not in Japanese, keep the original form. 

This is the Japanese text.
(1) achikara......「きたない」.おかしい,生意気なという意味をふくむ.
この物語は Okikirmui の父と pon nitnekamui の父とは,前に大層激しい戦争をしたことがあるので,この pon okikirmui と pon nitnekamui とは敵どうしになっています.その親たちの戦争した模様は別な物語に詳しく出ています.

This is the Chinese Translation 1.
(1) achikara......意指「骯髒」。帶有奇怪、自大的意味。
這個故事中,Okikirmui 的父親和 pon nitnekamui 的父親之前曾爆發過非常激烈的戰爭,因此 pon okikirmui 和 pon nitnekamui 之間是敵對關係。關於他們父輩戰爭的詳細情況,在另一個故事中有詳細描述。


This is the Chinese Translation 2.
(1) achikara...... "kitanai" [dirty/骯髒]. 包含奇怪、冒昧等含義。

在這個故事中，Okikirmui 的父親和 pon nitnekamui 的父親過去曾發生過非常激烈的戰爭，所以這個 pon okikirmui 和 pon nitnekamui 是敵人。他們父母之間戰爭的細節在另一個故事中有詳細描述。

```

### Output
```
(1) achikara......意指「骯髒 (kitanai)」。帶有奇怪、冒昧等含義。

在這個故事中，Okikirmui 的父親和 pon nitnekamui 的父親過去曾爆發過非常激烈的戰爭，因此 pon okikirmui 和 pon nitnekamui 之間是敵對關係。關於他們父輩戰爭的詳細情況，在另一個故事中有詳細描述。

Analysis of the two Chinese translations:

Translation 1:
Pros: More fluent and natural in Chinese.
Cons: Omits the original Japanese word "kitanai" and its English translation "dirty/骯髒", losing some original information.

Translation 2:
Pros: Includes the original Japanese word "kitanai" and its English translation "dirty/骯髒", preserving more original information.
Cons: Slightly less fluent than Translation 1.

Choice of Better Translation:
Translation 2 is slightly better because it preserves more of the original information by including "kitanai" and its translation. Accuracy is prioritized.

Updated Translation Strategy:
Incorporate the fluency of Translation 1 while retaining the key information from Translation 2. Use parentheses to clarify the meaning of "achikara".
```

