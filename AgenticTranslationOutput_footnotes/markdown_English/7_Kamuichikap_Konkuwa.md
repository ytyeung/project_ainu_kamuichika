# Project Ainu Kamuichika: LLM-assisted Translation of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Updated Chinese Translation of

## Kamuichikap Kamui yaieyukar, “Konkuwa” 
## 梟の神が自ら歌った謡「コンクワ」
## Translation of Ainu Chant Footnote

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
(1) katken......川ガラス.昔から大そういい鳥として尊ばれる鳥です.

This is the English Translation 1.
katken......River crow. It is a bird that has been highly respected as a very good bird since ancient times.

This is the English Translation 2.
katken......Dipper. It has been respected as a very good bird since ancient times.

```
### Scoring

|               | Accuracy | Easy to understand |  Total Score |
| ------------- | -------- | ------------------ | ------------ | 
| Translation 1 | 4 | 5 |  4.4 |
| Translation 2 | 5 | 5 |  5.0 |

### Comments
#### Translation 1
This translation is understandable and conveys the general meaning. However, "River crow" is not the most accurate translation of "川ガラス".

#### Translation 2
This translation is also understandable and conveys the meaning. "Dipper" is a more accurate translation of "川ガラス".

### Better Choice
Translation 2
#### Comment
Both translations are quite similar and accurate. Translation 2 uses "Dipper" which is a more precise translation of "川ガラス(kawa garasu)" than "River crow". Therefore, Translation 2 is slightly better.

### Updated Output
```
katken......Dipper. It is a bird that has been highly respected as a very good bird since ancient times.
```

