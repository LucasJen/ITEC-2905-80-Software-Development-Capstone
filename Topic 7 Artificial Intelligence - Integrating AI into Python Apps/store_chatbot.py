from google import genai
from google.genai.types import GenerateContentConfig
import rich
from rich.markdown import Markdown
import sys

client = genai.Client()
chat = client.chats.create(model='gemini-2.5-flash')

try:
    with open('chat_system_instructions.txt', 'r') as f:
        system_instructions_text = f.read()
except:
    print('missing system instruction, quitting.')

while True:
    question = input('Enter your message for the chatbot ')
    response = chat.send_message(
        # model='gemini-2.5-flash',
        question,
        config=GenerateContentConfig(
            system_instruction=system_instructions_text
        )
    )

    rich.print(Markdown(response.text))