# LLM-assisted Translation project of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Iterative 1 Updated Chinese Translation of

## Pon Okikirmui yaieyukar, “Kutnisa kutunkutun” 小オキキリムイが自ら歌った謡「クツニサ クトンクトン」

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


This is the Chinese Translation 1.
There is no numbered item in the provided content.


This is the Chinese Translation 2.
請提供您想要翻譯的英文文本，我會將其翻譯成現代標準漢語（繁體中文），並盡力保持原文含義。如果原文中包含無法翻譯的術語，我會保留其原始語言。

```

### Output
```
請提供日文原文以及兩個中文翻譯版本，以便我進行比較、分析優缺點、選擇較佳版本，並據此產生更完善的翻譯。（Please provide the original Japanese text and the two Chinese translations so I can compare them, analyze their pros and cons, choose the better version, and create a more complete translation.）

I cannot fulfill the request because the original Japanese text and the two Chinese translations are missing. Please provide the necessary information so I can compare the translations, identify their pros and cons, choose the better one, and create an improved translation.
```

