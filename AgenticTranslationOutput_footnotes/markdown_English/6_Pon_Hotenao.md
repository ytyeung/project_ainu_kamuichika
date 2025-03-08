# Project Ainu Kamuichika: LLM-assisted Translation of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Updated Chinese Translation of

## Pon Horkeukamui yaieyukar, “Hotenao” 
## 小狼の神が自ら歌った謡「ホテナオ」
## Ainu Chant Footnote Translation

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
Please provide the Japanese Ainu chant footnote text that needs to be translated.

```
### Scoring

|               | Accuracy | Easy to understand |  Total Score |
| ------------- | -------- | ------------------ | ------------ | 
| Translation 1 | 4 | 4 |  4.0 |
| Translation 2 | 3 | 5 |  3.8 |

### Comments
#### Translation 1
Translation 1 maintains a closer connection to the original Japanese, making it more suitable for understanding the nuances of the chant. It prioritizes accuracy over stylistic flair.

#### Translation 2
Translation 2 attempts a more poetic rendering, which can be helpful for conveying the spirit of the chant but sacrifices some accuracy in the details. It might be less useful for someone trying to understand the literal meaning of the footnotes.

### Better Choice
Translation 1
#### Comment
Translation 1 is better because it maintains a more literal connection to the original Japanese, which is crucial for understanding footnotes related to a chant. While Translation 2 attempts to be more poetic, it loses some of the directness and clarity needed for annotations. The weighted score reflects this preference for accuracy.

### Updated Output
```
Please provide the Japanese Ainu chant footnote text that needs to be translated, along with the two English translations you have.
```

