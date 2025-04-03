# Project Ainu Kamuichika: LLM-assisted Translation of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Updated Chinese Translation of

## Isepo yaieyukar, “Sampaya terke” 
## 兎が自ら歌った謡「サンパヤ テレケ」
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
(1) アマツポ(弩いしゆみ)すなわち「仕掛け弓」を仕掛ける事.
(2) 刀剣.これは戦争の時に使う刀剣とは違うので,ふだん家の右座の宝物の積んである上に吊してあるのがそれです.戦争の時には使いませんが,uniwente などのときには使います.

This is the English Translation 1.
(1) Amatsupo (a type of spring-loaded bow): This refers to setting up a "spring-loaded bow."
(2) Sword. This is different from the swords used in war. It is usually hung above the pile of treasures on the right side of the house. It is not used in times of war, but it is used during events such as uniwente.

This is the English Translation 2.
(1) アマツポ(弩いしゆみ), which means setting up the "automatic bow".
(2) Swords. These swords are different from those used in war. They are usually hung on the right side of the house where treasures are stored. They are not used in war, but are used in rituals such as uniwente.

```
### Scoring

|               | Accuracy | Easy to understand |  Total Score |
| ------------- | -------- | ------------------ | ------------ | 
| Translation 1 | 4 | 4 |  4.0 |
| Translation 2 | 4 | 4 |  4.0 |

### Comments
#### Translation 1
Pros: Clearly defines 'Amatsupo' as a type of spring-loaded bow. Cons: Could be more specific about 'uniwente' being a ritual.

#### Translation 2
Pros: More accurately translates '仕掛け弓' as 'automatic bow'. Cons: Less descriptive about 'Amatsupo'; uses 'Swords' (plural) which might be inaccurate if only one sword is referenced.

### Better Choice
Translation 1
#### Comment
Both translations are of similar quality. Translation 1 is chosen because it provides a clearer definition of 'Amatsupo'.

### Updated Output
```
(1) Amatsupo (弩いしゆみ, a type of spring-loaded bow): This refers to setting up the "automatic bow".
(2) Sword. This sword is different from the swords used in war. It is usually hung above the pile of treasures on the right side of the house. It is not used in times of war, but it is used during rituals such as uniwente.
```

