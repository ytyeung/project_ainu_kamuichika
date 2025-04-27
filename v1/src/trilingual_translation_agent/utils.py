from google import genai
from google.genai import types
import base64
import json
import os
from dotenv import load_dotenv

from pydantic import BaseModel, Field
from typing import Union, Dict

import unicodedata
import re
from .prompt import system_prompt, translation_prompt, reflection_prompt
from .schema import Translation, Reflection

import attr 

class TranslationAgent:
    def __init__(self, client: genai.Client, model: str,source_language :str, target_language_1: str, target_language_2:str):
        self.system_prompt = system_prompt.format(source_language = source_language, target_language_1=target_language_1, target_language_2=target_language_2)
        self.client = client
        self.model = model

    def generate_content_config(self,temperature :float, top_p :float, schema :BaseModel) -> types.GenerateContentConfig:
        generate_content_config = types.GenerateContentConfig(
            temperature = temperature,
            top_p = top_p,
            max_output_tokens = 8192,
            response_mime_type = 'application/json',
            response_schema = schema,
            safety_settings = [types.SafetySetting(
            category="HARM_CATEGORY_HATE_SPEECH",
            threshold="OFF"
            ),types.SafetySetting(
            category="HARM_CATEGORY_DANGEROUS_CONTENT",
            threshold="OFF"
            ),types.SafetySetting(
            category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
            threshold="OFF"
            ),types.SafetySetting(
            category="HARM_CATEGORY_HARASSMENT",
            threshold="OFF"
            )],
            system_instruction=[types.Part.from_text(text=self.system_prompt)],
        )

        return generate_content_config

    def generate(self,client: genai.Client,generate_content_config :types.GenerateContentConfig, model :str, /, prompt :str):

        text_full_prompt = types.Part.from_text(text=f"{prompt}")

        output = ""

        contents = [
        types.Content(
            role="user",
            parts=[
            text_full_prompt
            ]
        )
        ]

        for chunk in client.models.generate_content_stream(
            model = model,
            contents = contents,
            config = generate_content_config,
            ):
            #print(chunk.text, end="")
            output += chunk.text

        #print (output)

        return output

    def translation(self, prompt :Union[str, None] = None, temperature :float = 0, top_p :float = 0, 
                    input_data :Union[Dict, None] = None, model :Union[str, None] = None, schema :Union[BaseModel,None] = None):
        

        if prompt:
            input_prompt = prompt
        else:
            input_prompt = translation_prompt

        input_prompt = input_prompt.format(**input_data)

        if model:
            input_model = model
        else:
            input_model =self.model

        if schema:
            input_schema = schema
        else:
            input_schema = Translation

        #print(input_prompt)
        generate_content_config = self.generate_content_config(temperature = temperature, top_p = top_p, schema=input_schema)

        response = self.generate(self.client,generate_content_config, input_model, prompt = input_prompt)

        output = json.loads(response)
        output['system_prompt'] = self.system_prompt
        output['input_prompt'] = input_prompt
        output['input_model'] = input_model
        output['input_schema'] = input_schema.model_json_schema()
        output['generate_content_config'] = str(generate_content_config)

        return output
    
    def reflection_and_update_translation(self, prompt :Union[str, None] = None, temperature :float = 0, top_p :float = 0, 
                                          input_data :Union[Dict, None] = None, model :str = None, schema :Union[BaseModel,None] = None):

        if prompt:
            input_prompt = prompt
        else:
            input_prompt = translation_prompt

        input_prompt = input_prompt.format(**input_data)

        if model:
            input_model = model
        else:
            input_model =self.model

        if schema:
            input_schema = schema
        else:
            input_schema = Translation

        #print(input_prompt)
        generate_content_config = self.generate_content_config(temperature = temperature, top_p = top_p, schema=input_schema)

        response = self.generate(self.client,generate_content_config, input_model, prompt = input_prompt)

        output = json.loads(response)
        output['system_prompt'] = self.system_prompt
        output['input_prompt'] = input_prompt
        output['input_model'] = input_model
        output['input_schema'] = input_schema.model_json_schema()
        output['generate_content_config'] = str(generate_content_config)
        return output
    


