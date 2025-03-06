system_prompt="""You are a professional translator. 
You know {source_language}, {target_language_1} and {target_language_2}. 
You can translate {source_language} into either {target_language_1} or {target_language_2}. 
You can also translate {target_language_1} into {target_language_2}, and {target_language_2} into {target_language_1}.
"""

translation_prompt = """Translate the following text from {source_language} to {target_language}. 
Keep the original meaning. Only allow characters of {source_language} and {target_language}.
If a term cannot be translated, keep the original language.

{source_text}
"""

## Machine Translation quality estimation

# @inproceedings{kocmi-federmann-2023-large,
#     title = "Large Language Models Are State-of-the-Art Evaluators of Translation Quality",
#     author = "Kocmi, Tom and Federmann, Christian",
#     booktitle = "Proceedings of the 24th Annual Conference of the European Association for Machine Translation",
#     month = jun,
#     year = "2023",
#     address = "Tampere, Finland",
#     publisher = "European Association for Machine Translation",
#     url = "https://aclanthology.org/2023.eamt-1.19",
#     pages = "193--203",
# }

reflection_prompt = """You are translating the following {source_language} text into {target_language}. 
You have 2 versions of {target_language} translations at hand.

Here are your tasks:

1. Compare the two {target_language} translations with the original {source_language} text. List out the Pros and Cons of the Translations.
2. For each of translation from {source_language} to {target_language}, score the translation on the accuracy of original meaning with one to five stars [1,2,3,4,5].
Where one star means "Nonsense/No meaning preserved",
two stars mean "Some meaning preserved, but not understandable",
three stars mean "Some meaning preserved and understandable",
four stars mean "Most meaning preserved with possibly few grammar mistakes",
and five stars mean "Perfect meaning and grammar".

2. For each of translation from {source_language} to {target_language}, score the translation on the easiness to understanding with one to five stars [1,2,3,4,5].
Where one star means "The text is completely not understandable.",
two stars mean "Most part of text is not understandable.",
three stars mean "While the text is understandable, the word usage and grammar are difficult.",
four stars mean "Most part of text can be understood easily.",
and five stars mean "All part of text can be understood easily.".
4. Choose a better translation according to the weighted score. Accuracy of meaning is the most important criterion (60%). Easy to understand is the second (40%).
5. Based on the better translation, translate the {source_language} text into {target_language} again, incorporating the Pros of the two translations.

Keep the original meaning accurately.
If a term cannot be translated, keep the original language.

This is the {source_language} text.
{source_text}

This is the {target_language} Translation 1.
{translation_1}

This is the {target_language} Translation 2.
{translation_2}
"""
