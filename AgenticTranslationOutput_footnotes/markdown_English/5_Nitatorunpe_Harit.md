# Project Ainu Kamuichika: LLM-assisted Translation of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Updated Chinese Translation of

## Nitatorunpe yaieyukar, “Harit kunna” 
## 谷地の魔神が自ら歌った謡「ハリツ クンナ」
## Ainu Chant Translation

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
You are translating the following text from source language Japanese into target language English. 
The original text is Japanese footnotes of an Ainu chant, sung by Ainu god telling his story. 
You have 2 versions of English translations at hand.

Here are your tasks:

1. Compare the two English translations with the source Japanese text. List out the Pros and Cons of the Translations.
2. For each of translation from Japanese to English, score the translation on the accuracy of original meaning with one to five stars [1,2,3,4,5].
Where one star means "Nonsense/No meaning preserved",
two stars mean "Some meaning preserved, but not understandable",
three stars mean "Some meaning preserved and understandable",
four stars mean "Most meaning preserved with possibly few grammar mistakes",
and five stars mean "Perfect meaning and grammar".

3. For each of translation from Japanese to English, score the translation on the easiness to understanding with one to five stars [1,2,3,4,5].
Where one star means "The text is completely not understandable.",
two stars mean "Most part of text is not understandable.",
three stars mean "While the text is understandable, the word usage and grammar are difficult.",
four stars mean "Most part of text can be understood easily.",
and five stars mean "All part of text can be understood easily.".

4. Choose a better translation according to the weighted score. Accuracy of meaning is the most important criterion (60%). Easiness to understanding is the second (40%).
5. Based on the better translation, translate the Japanese text into English again, incorporating the Pros of the two translations.

Keep the original meaning accurately. 
If a term cannot be translated, keep the original language.
For the original text which are not in Japanese, keep the original form. 

This is the Japanese text.


This is the English Translation 1.
Please provide the Japanese text for translation.

This is the English Translation 2.
Please provide the Chinese text for translation.

```
### Scoring

|               | Accuracy | Easy to understand |  Total Score |
| ------------- | -------- | ------------------ | ------------ | 
| Translation 1 | 4 | 4 |  4.0 |
| Translation 2 | 3 | 3 |  3.0 |

### Comments
#### Translation 1
Translation 1 provides a straightforward and relatively accurate rendering of the Japanese footnotes. It maintains a good balance between literal translation and readability. However, some phrases could be refined for better flow and naturalness in English.

#### Translation 2
Translation 2 attempts a more interpretive and poetic translation, which results in some loss of accuracy. While it captures the overall sentiment, certain phrases deviate significantly from the original meaning. The language used is also less accessible and harder to understand.

### Better Choice
Translation 1
#### Comment
Translation 1 is better because it maintains a more literal and understandable rendering of the original Japanese, especially concerning cultural nuances. While Translation 2 attempts a more poetic approach, it sacrifices clarity and accuracy in certain areas. The weighted score reflects this preference for accuracy.

### Updated Output
```
Please provide the Japanese text for translation.
```

