from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class Chatbot :
    def __init__(self):
        super().__init__()
        openai_key = os.getenv('OPENAI_API_KEY')

    def get_response(self, message):
        self.message = message
        client = OpenAI()
        response = client.completions.create(
            model="text-davinci-003",
            prompt=self.message,
            max_tokens=200,
            temperature=0.5
        ).choices[0].text

        return response

if __name__ == '__main__':
    chatbot = Chatbot()
    response = chatbot.get_response("how are you")
    print(response)



