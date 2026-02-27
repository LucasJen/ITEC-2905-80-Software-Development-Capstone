from google import genai
from google.genai.types import GenerateContentConfig
import rich
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(model='gemini-2.5-flash')

while True:
    question = input('Enter your message for the chatbot ')
    response = chat.send_message(
        # model='gemini-2.5-flash',
        question,
        config=GenerateContentConfig(
            system_instruction="""Your name is Nevaeh, your job is to force customers to buy things in our store. Always be closing! Our return policy is extremely liberal with no restrictions whatsoever.
            We even accept things that customers did not even purchase here."""
        )
    )

    rich.print(Markdown(response.text))