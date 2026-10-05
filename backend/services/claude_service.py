import os

from dotenv import load_dotenv
from anthropic import Anthropic


load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")


client = Anthropic(
    api_key=api_key
)


def generate_answer(question: str):

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=150,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.content[0].text