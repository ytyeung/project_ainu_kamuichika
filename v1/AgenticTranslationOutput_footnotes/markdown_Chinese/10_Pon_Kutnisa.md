# Project Ainu Kamuichika: LLM-assisted Translation of Ainu shin'yoshu (アイヌ神謡集) collected by Chiri Yukie 知里幸惠 (1903 - 1922).

## Updated Chinese Translation of

## Pon Okikirmui yaieyukar, “Kutnisa kutunkutun” 
## 小オキキリムイが自ら歌った謡「クツニサ クトンクトン」
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
(1) iwan poknashir......六つの地獄.地の下には六段の世界があってそこには種々な悪魔が住んでいます.

This is the Chinese Translation 1.
iwan poknashir......六個地獄。地的下面有六層世界，那裡住著各種各樣的惡魔。

This is the Chinese Translation 2.
iwan poknashir......六層地獄。地下有六層世界，住著各種惡魔。

```
### Scoring

|               | Accuracy | Easy to understand |  Total Score |
| ------------- | -------- | ------------------ | ------------ | 
| Translation 1 | 4 | 4 |  4.0 |
| Translation 2 | 4 | 5 |  4.4 |

### Comments
#### Translation 1
翻譯1使用了“六個地獄”，更接近原文的字面意思，但可能在現代漢語語境下稍顯不自然。使用了“各種各樣的惡魔”，更強調種類的繁多。

#### Translation 2
翻譯2使用了“六層地獄”，更符合中文的表達習慣，更自然。使用了“各種惡魔”，簡潔明瞭。

### Better Choice
Translation 2
#### Comment
翻譯2在易於理解方面略勝一籌，更符合現代漢語的表達習慣。雖然翻譯1在字面意思上更接近原文，但翻譯2在整體語感上更流暢自然。

### Updated Output
```
iwan poknashir......六層地獄。地的下面有六層世界，那裡住著各種各樣的惡魔。
```

