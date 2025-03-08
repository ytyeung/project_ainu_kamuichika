# Project Ainu Kamuichika: LLM-assisted Translation of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Updated Chinese Translation of

## Isepo yaieyukar, “Sampaya terke” 
## 兎が自ら歌った謡「サンパヤ テレケ」
## Ainu Chant Footnotes Translation

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
(1) アマツポ(弩いしゆみ)すなわち「仕掛け弓」を仕掛ける事.
(2) 刀剣.これは戦争の時に使う刀剣とは違うので,ふだん家の右座の宝物の積んである上に吊してあるのがそれです.戦争の時には使いませんが,uniwente などのときには使います.

This is the English Translation 1.
(1) Amatsupo (弩いしゆみ): This means setting up a "trick bow."
(2) Sword: This is different from the swords used in war. It is usually hung above the pile of treasures in the right seat of the house. It is not used in war, but it is used during events such as uniwente.

This is the English Translation 2.
(1) アマツポ (crossbow): This means setting up a "machine bow."
(2) Swords. These are different from the swords used in war. They are usually hung on the right side of the house where treasures are stored. They are not used in war, but are used in rituals such as uniwente.

```
### Scoring

|               | Accuracy | Easy to understand |  Total Score |
| ------------- | -------- | ------------------ | ------------ | 
| Translation 1 | 3 | 4 |  3.4 |
| Translation 2 | 4 | 4 |  4.0 |

### Comments
#### Translation 1
Translation 1 uses 'trick bow' which is not as accurate as 'crossbow'. It also uses 'events' which is a less accurate translation of the context than 'rituals'.

#### Translation 2
Translation 2 uses 'crossbow' which is a more accurate translation of \"弩いしゆみ\". It also uses \"rituals\" which is a better fit for \"uniwente\" than \"events\".

### Better Choice
Translation 2
#### Comment
Translation 2 uses 'crossbow' which is a more accurate translation of \"弩いしゆみ\" than \"trick bow\". It also uses \"rituals\" which is a better fit for \"uniwente\" than \"events\". The grammar in Translation 2 is also slightly better.

### Updated Output
```
(1) Amatsupo (crossbow): This refers to setting up a "machine bow."
(2) Sword: These are different from the swords used in war. They are usually hung above the pile of treasures on the right side of the house. They are not used in war, but are used during rituals such as uniwente.
```

