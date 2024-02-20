from openai import OpenAI
from dotenv import dotenv_values
from database import DBClient
from open_ai.model import Prompt


config = dotenv_values(".env")


class OpenAIClient(OpenAI):
    def __init__(self, openai_api_key: str):
        super().__init__(api_key=openai_api_key)

    def chat_completion(self, prompt: Prompt) -> str:
        completion = self.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "system", "content": "You are a talkative AI assistant"},
                {"role": "user", "content": prompt.text}
            ],
            max_tokens=500,
            temperature=0.5,
        )

        return completion.choices[0].message.content

    def speech_to_text(self, mp3_file) -> any:
        with open(mp3_file, 'rb') as file:
            transcript = self.audio.transcriptions.create(
                model='whisper-1',
                file=file,
                response_format='text',
            )
        return transcript


