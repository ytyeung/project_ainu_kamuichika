from pydantic import BaseModel, Field

class Translation(BaseModel):
    """The translation, and the comments"""
    translation: str = Field(description="The translation")
    title: str = Field(description="The translated title")
    comment: str = Field(description="Comments on the translation")

class Comment(BaseModel):
    id: str = Field(description="For example: Translation 1 or Translation 2")
    comment: str = Field(description="comment of the translation")

class Score(BaseModel):
    id: str = Field(description="For example: Translation 1 or Translation 2")
    score_accuracy: int = Field(description="Accuracy score of the translation")
    score_easy_understanding :int = Field(description="easiness to understanding score of the translation")
    weighted_score: float = Field(description="weighted score of the translation")

class Reflection(BaseModel):
    """The updated translation, and the comments for the update"""
    title: str = Field(description="The translated title")
    translation_comments: list[Comment] = Field(description="Comments of all translations")
    translation_scores: list[Score] = Field(description="Scores of all translations")

    better_translation:  str = Field(description="For example: Translation 1 or Translation 2")
    better_translation_comment: str = Field(description="Explanation of better translation choice.")
    updated_translation: str = Field(description="Updated Translation")

    