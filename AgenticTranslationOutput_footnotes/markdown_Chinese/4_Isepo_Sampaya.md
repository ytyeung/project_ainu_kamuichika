# Project Ainu Kamuichika: LLM-assisted Translation of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Updated Chinese Translation of

## Isepo yaieyukar, “Sampaya terke” 
## 兎が自ら歌った謡「サンパヤ テレケ」
## 阿伊努語聖歌腳註翻譯

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
(1) アマツポ(弩いしゆみ)すなわち「仕掛け弓」を仕掛ける事.
(2) 刀剣.これは戦争の時に使う刀剣とは違うので,ふだん家の右座の宝物の積んである上に吊してあるのがそれです.戦争の時には使いませんが,uniwente などのときには使います.

This is the Chinese Translation 1.
(1) アマツポ(弩いしゆみ)，即架設「機關弓」。
(2) 刀劍。這和戰爭時使用的刀劍不同，平時吊在房屋右側堆放寶物的地方。戰爭時不會使用，但在uniwente等儀式時會使用。

This is the Chinese Translation 2.
(1) Amatsupo (弩いしゆみ)：這意味著設置一個「機關弓」。
(2) 劍：這與戰爭中使用的劍不同。它通常懸掛在房屋右側座位上的寶物堆之上。它不用於戰爭，但用於 uniwente 等活動中。

```
### Scoring

|               | Accuracy | Easy to understand |  Total Score |
| ------------- | -------- | ------------------ | ------------ | 
| Translation 1 | 5 | 4 |  4.6 |
| Translation 2 | 4 | 5 |  4.4 |

### Comments
#### Translation 1
Translation 1 is concise and accurately conveys the meaning. The use of 「機關弓」is appropriate.

#### Translation 2
Translation 2 is also accurate but slightly wordier. The explanation of Amatsupo is a bit redundant.

### Better Choice
Translation 1
#### Comment
Translation 1 is more concise and direct in its explanation of 'アマツポ'. It also maintains a slightly more formal tone, which might be appropriate for footnotes referencing a religious chant. While both translations are generally good, Translation 1 edges out Translation 2 due to its conciseness and tone.

### Updated Output
```
(1) アマツポ(弩いしゆみ)，即架設「機關弓」。
(2) 刀劍。這和戰爭時使用的刀劍不同，平時吊在房屋右側堆放寶物的地方。戰爭時不會使用，但在uniwente等儀式時會使用。
```

