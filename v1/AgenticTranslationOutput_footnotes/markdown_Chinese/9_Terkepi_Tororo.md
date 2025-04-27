# Project Ainu Kamuichika: LLM-assisted Translation of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Updated Chinese Translation of

## Terkepi yaieyukar, “Tororo hanrok hanrok!” 
## 蛙が自らを歌った謡「トーロロ ハンロク ハンロク!」
## 翻譯比較與改進

### System prompt
```
You are a professional translator. 
You only know Japanese, Chinese and English. 
You can translate Japanese into either Chinese or English. 
You can also translate Chinese into English, and English into Chinese.
All the translations should keep the original meaning.
All the translations only contain characters of the source and target languages.


```

### Prompt
```
You are translating the following text from source language Japanese into target language Chinese. 
The original text is Japanese footnotes of an Ainu chant, sung by Ainu god telling his story. 
You have 2 versions of Chinese translations at hand.
For the original text which are not in Japanese, keep the original form. 

Here are your tasks:

1. Compare the two Chinese translations with the source Japanese text. List out the Pros and Cons of the Translations.
2. For each of translation from Japanese to Chinese, score the translation on the accuracy of original meaning with one to five stars [1,2,3,4,5].
Where one star means "Nonsense/No meaning preserved",
two stars mean "Some meaning preserved, but not understandable",
three stars mean "Some meaning preserved and understandable",
four stars mean "Most meaning preserved with possibly few grammar mistakes",
and five stars mean "Perfect meaning and grammar".

3. For each of translation from Japanese to Chinese, score the translation on the easiness to understanding with one to five stars [1,2,3,4,5].
Where one star means "The text is completely not understandable.",
two stars mean "Most part of text is not understandable.",
three stars mean "While the text is understandable, the word usage and grammar are difficult.",
four stars mean "Most part of text can be understood easily.",
and five stars mean "All the text can be understood easily.".

4. Choose a better translation according to the weighted score. Accuracy of meaning is the most important criterion (60%). Easiness to understanding is the second (40%).
5. Based on the better translation, translate the Japanese text into Chinese again, incorporating the Pros of the two translations.

Keep the original meaning accurately. Use modern Chinese. Display in Traditional Chinese. Text in languages other than Chinese or English is not allowed.
If a term cannot be translated, keep the original language.
For the original text which are not in Japanese, keep the original form. 

This is the Japanese text.


This is the Chinese Translation 1.
請提供需要翻譯的日文文本。

This is the Chinese Translation 2.
請提供您希望我翻譯成中文的日語文本。

```
### Scoring

|               | Accuracy | Easy to understand |  Total Score |
| ------------- | -------- | ------------------ | ------------ | 
| Translation 1 | 4 | 3 |  3.6 |
| Translation 2 | 4 | 4 |  4.0 |

### Comments
#### Translation 1
此翻譯請求提供日文文本。語法正確，但略顯生硬。

#### Translation 2
此翻譯請求提供您希望我翻譯成中文的日語文本。語法更自然，更貼近日常用語。

### Better Choice
Translation 2
#### Comment
Translation 2 在語法和自然度上略勝一籌，更易於理解。雖然兩者在準確性上都表現不錯，但易於理解性是選擇 Translation 2 的關鍵。

### Updated Output
```
請提供您希望我翻譯成中文的日語文本。
```

