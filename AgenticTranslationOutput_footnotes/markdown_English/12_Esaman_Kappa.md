# Project Ainu Kamuichika: LLM-assisted Translation of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Updated Chinese Translation of

## Esaman yaieyukar, “Kappa reureu kappa” 
## 獺かわうそが自ら歌った謡「カッパ レウレウ カッパ」
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
(1) achikara......「きたない」.おかしい,生意気なという意味をふくむ.
この物語は Okikirmui の父と pon nitnekamui の父とは,前に大層激しい戦争をしたことがあるので,この pon okikirmui と pon nitnekamui とは敵どうしになっています.その親たちの戦争した模様は別な物語に詳しく出ています.

This is the English Translation 1.
achikara......"dirty." It includes meanings such as strange and cheeky.
In this story, Okikirmui's father and pon nitnekamui's father had a very fierce war before, so this pon okikirmui and pon nitnekamui are enemies. The details of the war between their parents are described in detail in another story.

This is the English Translation 2.
(1) achikara......"Dirty." It contains the meanings of strange and arrogant.
This story is about Okikirmui's father and pon nitnekamui's father having a very fierce war before, so this pon okikirmui and pon nitnekamui are in a hostile relationship. The appearance of their parents' war is described in detail in another story.

```
### Scoring

|               | Accuracy | Easy to understand |  Total Score |
| ------------- | -------- | ------------------ | ------------ | 
| Translation 1 | 4 | 4 |  4.0 |
| Translation 2 | 5 | 4 |  4.6 |

### Comments
#### Translation 1
Translation 1 uses 'dirty' which is a direct translation of きたない. It uses 'cheeky' to translate 生意気, which is not accurate. It also uses 'enemies' which is not as descriptive as 'hostile relationship'.

#### Translation 2
Translation 2 uses 'dirty' which is a direct translation of きたない. It uses 'arrogant' to translate 生意気, which is more accurate. It also uses 'hostile relationship' which is a more natural way to describe the relationship between the two pon.

### Better Choice
Translation 2
#### Comment
Translation 2 uses 'arrogant' which is closer to the original meaning of 生意気 than 'cheeky'. It also uses 'hostile relationship' which is a more natural way to describe the relationship between the two pon.

### Updated Output
```
(1) achikara......"dirty." It includes meanings such as strange and arrogant. This story is about Okikirmui's father and pon nitnekamui's father having a very fierce war before, so this pon okikirmui and pon nitnekamui are in a hostile relationship. The details of their parents' war are described in detail in another story.
```

