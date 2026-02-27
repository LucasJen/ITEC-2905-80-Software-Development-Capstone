from google import genai
from google.genai.types import GenerateContentConfig
import rich
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(model='gemini-2.5-flash')

while True:
    question = input('Enter your message for the tutor')
    response = chat.send_message(
        # model='gemini-2.5-flash',
        question,
        config=GenerateContentConfig(
            system_instruction="""You a helpful programming tutor for Java programming students. You can explain concepts and programs, but don't give direct answers."""
        )
    )

    rich.print(Markdown(response.text))