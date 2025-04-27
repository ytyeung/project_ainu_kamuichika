from pydantic import BaseModel, Field

# Schema for the translation results
class Translation(BaseModel):
    """The translation, and the comment"""
    translation: str = Field(description="The translation")
    title: str = Field(description="The translated title")
    comment: str = Field(description="Comments on the translation")
    agent: str = Field(description="The agent who generates the translation")
    text_type: str = Field(description="The type of text, for example: main story, footnote, prologue, etc.")

class Score(BaseModel):
    id: str = Field(description="For example: Translation 1 or Translation 2")
    agent: str = Field(description="The agent who generates the translation")
    text_type: str = Field(description="The type of text, for example: main story, footnote, prologue, etc.")
    title: str = Field(description="The translated title")
    text: str = Field(description="The translated text")
    score_accuracy: int = Field(description="Accuracy score of the translation")
    score_easy_understanding :int = Field(description="easiness to understanding score of the translation")
    score_poetic_flow :int = Field(description="Level of poetic flow of the translation")
    weighted_score: float = Field(description="weighted score of the translation")
    comment: str = Field(description="comment of the score of the translation")

# Schema for the reflection outputs
class Reflection(BaseModel):
    """The updated translation, and the comments for the update"""
    translation_score: list[Score] = Field(description="Comments of all translations")
    better_translation:  str = Field(description="For example: Translation 1 or Translation 2")
    better_translation_comment: str = Field(description="Explanation of better translation choice.")
    agent: str = Field(description="The agent who generates the reflection report")
    
