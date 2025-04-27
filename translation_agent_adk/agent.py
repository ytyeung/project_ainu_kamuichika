from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
import os
from . import config, prompt, schema

# Translation Agent: Japanese to Chinese
translation_ja_zh_agent = LlmAgent(
    name="TranslationAgent_JA_to_ZH",
    model=os.getenv('GEMINI_MODEL'),
    instruction=f"""{prompt.system_prompt}

{prompt.translation_prompt_ja_to_zh}
""",
    description="Translates Japanese text to Chinese.",
    generate_content_config = config.generate_content_config,
    # Store result in state for the merger agent
    output_key="translation_result_ja_to_zh",
    output_schema=schema.Translation,
)

#Translation Agent: Japanese to English
translation_ja_en_agent = LlmAgent(
    name="TranslationAgent_JA_to_EN",
    model=os.getenv('GEMINI_MODEL'),
    instruction=f"""{prompt.system_prompt}

{prompt.translation_prompt_ja_to_en}
""",
    description="Translates Japanese text to English.",
    generate_content_config = config.generate_content_config,
    # Store result in state for the merger agent
    output_key="translation_result_ja_to_en",
    output_schema=schema.Translation,
)

#Translation Agent: English to Chinese
translation_en_zh_agent = LlmAgent(
    name="TranslationAgent_EN_to_ZH",
    model=os.getenv('GEMINI_MODEL'),
    instruction=f"""{prompt.system_prompt}

{prompt.translation_prompt_en_to_zh}

**Here is the English text in JSON:**

{{translation_result_ja_to_en}}

""",
    description="Translates English text to Chinese.",
    generate_content_config = config.generate_content_config,
    # Store result in state for the merger agent
    output_key="translation_result_en_to_zh",
    output_schema=schema.Translation,
)

#Translation Agent: Chinese to English
translation_zh_en_agent = LlmAgent(
    name="TranslationAgent_ZH_to_EN",
    model=os.getenv('GEMINI_MODEL'),
    instruction=f"""{prompt.system_prompt}

{prompt.translation_prompt_zh_to_en}

**Here is the Chinese text in JSON:**
{{translation_result_ja_to_zh}}

""",
    description="Translates Chinese text to English.",
    generate_content_config = config.generate_content_config,
    # Store result in state for the merger agent
    output_key="translation_result_zh_to_en",
    output_schema=schema.Translation,
)

#Reflection Agent: Chinese Translation
reflection_zh_agent = LlmAgent(
    name="ReflectionAgent_Chinese_Translation",
    model=os.getenv('GEMINI_MODEL'),
    instruction=f"""{prompt.system_prompt}

{prompt.zh_reflection_prompt}

This is the Chinese Translation 1.

{{translation_result_ja_to_zh}}

This is the Chinese Translation 2.

{{translation_result_en_to_zh}}

""",
    description="Reflection agent for 2 versions of Chinese translation.",
    generate_content_config = config.generate_content_config,
    # Store result in state for the merger agent
    output_key="reflection_result_zh",
    output_schema=schema.Reflection,
)

#Reflection Agent: English Translation
reflection_en_agent = LlmAgent(
    name="ReflectionAgent_English_Translation",
    model=os.getenv('GEMINI_MODEL'),
    instruction=f"""{prompt.system_prompt}

{prompt.en_reflection_prompt}

This is the English Translation 1.

{{translation_result_ja_to_en}}

This is the English Translation 2.

{{translation_result_zh_to_en}}

""",
    description="Reflection agent for 2 versions of English translation.",
    generate_content_config = config.generate_content_config,
    # Store result in state for the merger agent
    output_key="reflection_result_en",
    output_schema=schema.Reflection,
)

retranslation_zh_agent = LlmAgent(
    name="Retranslation_Chinese_Agent",
    model=os.getenv('GEMINI_MODEL'),
    instruction=f"""{prompt.system_prompt}


{prompt.zh_retranslation_prompt}

**Here is the reflection result in JSON:**

{{reflection_result_zh}}
""",
    description="Re-translation agent by combining the Pros of the 2 versions of Chinese translation.",
    generate_content_config = config.generate_content_config,
    # Store result in state for the merger agent
    output_key="re_translation_result_zh",
    output_schema=schema.Translation,
)

retranslation_en_agent = LlmAgent(
    name="Retranslation_English_Agent",
    model=os.getenv('GEMINI_MODEL'),
    instruction=f"""{prompt.system_prompt}

{prompt.en_retranslation_prompt}

**Here is the reflection result in JSON:**

{{reflection_result_en}}
""",
    description="Re-translation agent by combining the Pros of the 2 versions of English translation.",
    generate_content_config = config.generate_content_config,
    # Store result in state for the merger agent
    output_key="re_translation_result_en",
    output_schema=schema.Translation,
)


sequence_translation_ja_en_zh_agent = SequentialAgent(
    name="SequenceTranslationAgent_ZH",
    sub_agents=[translation_ja_en_agent, translation_en_zh_agent],
    description="This agent produces alternative Chinese translations from an English translation of Japanese text.",
)

sequence_translation_ja_zh_en_agent = SequentialAgent(
    name="SequenceTranslationAgent_EN",
    sub_agents=[translation_ja_zh_agent, translation_zh_en_agent],
    description="This agent produces alternative English translations from a Chinese translation of Japanese text.",
)

parallel_translation_agent = ParallelAgent(
    name="ParallelTranslationAgent",
    sub_agents=[sequence_translation_ja_zh_en_agent, sequence_translation_ja_en_zh_agent],
    description="This agent produces 2 versions of Chinese and English translations from Japanese text. The first one is from direct translation of Japanese text, another one is from an English translation of Japanese text.",
)

sequence_reflection = SequentialAgent(
    name="SequenceReflectionAgent",
    sub_agents=[parallel_translation_agent, reflection_zh_agent,retranslation_zh_agent, reflection_en_agent,retranslation_en_agent],
    description="This agent re-translates the Japanese text into Chinese and English based on the reflection comments.",
)


#root_agent = parallel_translation_ja_zh_agent
#root_agent = sequence_translation_ja_en_zh_agent
root_agent = sequence_reflection

