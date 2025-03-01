# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

## Isepo yaieyukar, “Sampaya terke” 兎が自ら歌った謡「サンパヤ テレケ」

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
(1) アマツポ(弩いしゆみ)すなわち「仕掛け弓」を仕掛ける事.
(2) 刀剣.これは戦争の時に使う刀剣とは違うので,ふだん家の右座の宝物の積んである上に吊してあるのがそれです.戦争の時には使いませんが,uniwente などのときには使います.

This is the Chinese Translation 1.
(1) アマツポ(弩いしゆみ),即「機關弓」的設置。
(2) 刀劍。此與戰爭時使用的刀劍不同,平時是吊在家中右座堆放寶物之處。戰爭時不會使用,但在 uniwente 等場合會使用。


This is the Chinese Translation 2.
（1）Amatsupo (弩いしゆみ)：意即設置一個「機關弓」。
（2）劍。這些與戰爭中使用的劍不同。它們通常懸掛在房屋右側的寶物堆之上。它們不用於戰爭，而是用於 *uniwente* 等場合。

```

### Output
```
（1）アマツポ(弩いしゆみ)：意即設置「機關弓」。
（2）刀劍。此刀劍與戰爭時所用刀劍不同，平時懸掛於家中右座堆放寶物之處。戰爭時不會使用，但在uniwente等場合會使用。

Analysis of the two Chinese translations:

Translation 1:
Pros: More concise in (1).
Cons: Less detailed in (1), using Japanese term directly without explanation. Less descriptive in (2).

Translation 2:
Pros: More detailed explanation in (1), providing the original Japanese term. More descriptive in (2).
Cons: Slightly wordy in (1).

Choice:
Translation 2 is better because it provides more context and explanation, which is crucial for understanding the original meaning accurately. It also retains the original Japanese term, which can be helpful for those familiar with the Ainu language.

Updated Translation Strategy:
Combine the conciseness of Translation 1 with the detail of Translation 2. Keep the original Japanese term and provide a clear explanation. Use more descriptive language in (2) while maintaining clarity.
```

