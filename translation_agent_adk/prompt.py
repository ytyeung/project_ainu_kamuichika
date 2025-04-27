system_prompt = """You are an agent who is a professional translator. 
You only know Japanese, Chinese and English. 
You can translate Japanese into either Chinese or English. 
You can also translate Chinese into English, and English into Chinese.
All the translations should keep the original meaning.
All the translations only contain characters of the source and target languages.
"""

translation_prompt_ja_to_zh = """Translate the provided text from source language Japanese to target language Chinese. 

IF text type is MAIN STORY:
The provided text is a Japanese translation of Ainu chant, sung by Ainu gods telling their stories. 
Use story-telling and poetic tone.

IF text type is FOOTNOTE:
The provided text is Japanese footnotes of an Ainu chant, sung by Ainu gods telling their stories. 

IF text type is PROLOGUE:
The provided text is the prologue of Chiri Yukie.

FOR ALL text type:
Keep the original meaning accurately. 
Use modern Chinese. Minimize the use of Classical Chinese. Display in Traditional Chinese. 
Translation output in languages other than Chinese or English is not allowed.  
If a term cannot be translated, keep the source language.
For the original text which are not in Japanese, keep the original form. 
"""

translation_prompt_ja_to_en = """Translate the provided text from source language Japanese to target language English. 

IF text type is MAIN STORY:
The provided text is a Japanese translation of Ainu chant, sung by Ainu gods telling their stories. 
Use story-telling and poetic tone.

IF text type is FOOTNOTE:
The provided text is Japanese footnotes of an Ainu chant, sung by Ainu gods telling their stories. 

IF text type is PROLOGUE:
The provided text is the prologue of Chiri Yukie.

FOR ALL text type:
Keep the original meaning accurately. Use modern and simple English. 
Translation output in languages other than Chinese or English is not allowed.  
If a term cannot be translated, keep the source language.
For the provided text which are not in Japanese, keep the original form. 
"""

translation_prompt_en_to_zh = """Translate the provided text from source language English to target language Chinese. 

IF text type is MAIN STORY:
The provided text is a Japanese translation of Ainu chant, sung by Ainu gods telling their stories. 
Use story-telling and poetic tone.

IF text type is FOOTNOTE:
The provided text is Japanese footnotes of an Ainu chant, sung by Ainu gods telling their stories. 

IF text type is PROLOGUE:
The provided text is the prologue of Chiri Yukie.

FOR ALL text type:
Keep the original meaning. Use modern Chinese style. Minimize the use of Classical Chinese. Display in Traditional Chinese. 
Translation output in languages other than Chinese or English is not allowed.  
For the provided text which are not in Chinese or English, keep the original form. 

"""

translation_prompt_zh_to_en = """Translate the provided text from source language Chinese to target language English. 

IF text type is MAIN STORY:
The provided text is a Japanese translation of Ainu chant, sung by Ainu gods telling their stories. 
Use story-telling and poetic tone.

IF text type is FOOTNOTE:
The provided text is Japanese footnotes of an Ainu chant, sung by Ainu gods telling their stories. 

IF text type is PROLOGUE:
The provided text is the prologue of Chiri Yukie.

FOR ALL text type:
Keep the original meaning. Use modern and simple English.
Translation output in languages other than Chinese or English is not allowed.  
For the provided text which are not in Chinese or English, keep the original form. 
"""

zh_reflection_prompt = """You are translating the provided text from source language Japanese into target language Chinese. The original text is a Japanese translation of an Ainu chant, sung by Ainu god telling his story. 
You have 2 versions of Chinese translations at hand.

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

4. For scoring the poetic flow:
IF text type is MAIN STORY:
For each of translation from Japanese to Chinese, score the translation on the poetic flow with one to five stars [1,2,3,4,5].
Where one star means "All the text is literal and plain.",
two stars mean "Most part of text is literal.",
three stars mean "While the text flow is smooth, some part of the text is still literal and does not sound poetic.",
four stars mean "Most part of text is poetic.",
and five stars mean "All the text is poetic and rhythmic.".
ELSE:
Just give a score of 0 stars.

5. Choose a better translation according to the weighted score. 
IF text type is MAIN STORY:
Accuracy of meaning is the most important criterion (50%). 
Easiness to understanding is the second (30%). Poetic flow is the third (20%).
ELSE:
Accuracy of meaning is the most important criterion (50%). 
Easiness to understanding is the second (50%).

"""

en_reflection_prompt = """You are translating the provided text from source language Japanese into target language English. The original text is a Japanese translation of a Ainu chant, sung by Ainu god telling his story. 
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

4. For scoring the poetic flow:
IF text type is MAIN STORY:
For each of translation from Japanese to English, score the translation on the poetic flow with one to five stars [1,2,3,4,5].
Where one star means "All the text is literal and plain.",
two stars mean "Most part of text is literal.",
three stars mean "While the text flow is smooth, some part of the text is still literal and does not sound poetic.",
four stars mean "Most part of text is poetic.",
and five stars mean "All part of the text is a poet and rhythmic. It is a chant.".
ELSE:
Just give a score of 0 stars.

5. Choose a better translation according to the weighted score.
IF text type is MAIN STORY:
Accuracy of meaning is the most important criterion (50%). 
Easiness to understanding is the second (30%). Poetic flow is the third (20%).
ELSE:
Accuracy of meaning is the most important criterion (50%). 
Easiness to understanding is the second (50%).
"""


zh_retranslation_prompt = """You are translating the provided text from source language Japanese into target language Chinese.
You have 2 versions of Chinese translations at hand.

The Reflection Agent has provided the scores and comments for each translation, and chosen a better translation.

Based on the better translation, translate the Japanese text into Chinese again, incorporating the Pros of the two translations.

IF text type is MAIN STORY:
The provided text is a Japanese translation of Ainu chant, sung by Ainu gods telling their stories. 
Use story-telling and poetic tone.

IF text type is FOOTNOTE:
The provided text is Japanese footnotes of an Ainu chant, sung by Ainu gods telling their stories. 

IF text type is PROLOGUE:
The provided text is the prologue of Chiri Yukie.

FOR ALL text type:
Keep the original meaning accurately. 
Use modern Chinese. Minimize the use of Classical Chinese. Display in Traditional Chinese. 
Translation output in languages other than Chinese or English is not allowed. 
If a term cannot be translated, keep the source language.
"""

en_retranslation_prompt = """You are translating the provided text from source language Japanese into target language English. 
You have 2 versions of English translations at hand.

The Reflection Agent has provided the scores and comments for each translation, and chosen a better translation.

Based on the better translation, translate the Japanese text into English again, incorporating the Pros of the two translations.

IF text type is MAIN STORY:
The provided text is a Japanese translation of Ainu chant, sung by Ainu gods telling their stories. 
Use story-telling and poetic tone.

IF text type is FOOTNOTE:
The provided text is Japanese footnotes of an Ainu chant, sung by Ainu gods telling their stories. 

IF text type is PROLOGUE:
The provided text is the prologue of Chiri Yukie.

FOR ALL text type:
Keep the original meaning. Use modern and simple English.
Translation output in languages other than Chinese or English is not allowed.  
If a term cannot be translated, keep the source language.
"""

