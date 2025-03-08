# Project Ainu Kamuichika: LLM-assisted Translation of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Updated Chinese Translation of

## Kamuichikap Kamui yaieyukar, “Konkuwa” 
## 梟の神が自ら歌った謡「コンクワ」
## 阿伊努語歌翻譯

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
(1) katken......川ガラス.昔から大そういい鳥として尊ばれる鳥です.

This is the Chinese Translation 1.
katken......河乌鸦。自古以来就被尊为非常好的鸟。

This is the Chinese Translation 2.
katken......河烏鴉。自古以來，牠們就被視為非常吉祥的鳥類，備受尊敬。

```
### Scoring

|               | Accuracy | Easy to understand |  Total Score |
| ------------- | -------- | ------------------ | ------------ | 
| Translation 1 | 4 | 4 |  4.0 |
| Translation 2 | 5 | 5 |  5.0 |

### Comments
#### Translation 1
This translation is a direct and literal rendering of the Japanese text. While accurate, it lacks some of the cultural nuance present in the original Japanese.

#### Translation 2
This translation captures the reverence associated with the bird more effectively by using "非常吉祥的鳥類，備受尊敬". It also uses "牠們" which is more accurate.

### Better Choice
Translation 2
#### Comment
Translation 2 is better because it provides a more nuanced and culturally sensitive translation of the phrase "大そういい鳥として尊ばれる鳥です". It uses "非常吉祥的鳥類，備受尊敬" which conveys a stronger sense of reverence and auspiciousness compared to the more literal "非常好的鸟" in Translation 1. Also, Translation 2 uses "牠們" which is more accurate.

### Updated Output
```
katken......河烏鴉。自古以來，牠們就被視為非常吉祥的鳥類，備受尊敬。
```

