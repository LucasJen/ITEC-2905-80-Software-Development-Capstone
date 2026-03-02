from google import genai
import rich
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(model='gemini-2.5-flash')

# Loop allows repeated interaction with chatback
while True:
    prompt = input('Enter your message: ')
    response = chat.send_message(prompt + 'Answer in a short sentence')
    rich.print(Markdown(response.text))
    # prints token usage
    print(response.usage_metadata.total_token_count)
    
# response = client.models.generate_content(
#     model='gemini-2.5-flash',
#     contents='Why is the sky blue?'
# )


# print(response.usage_metadata)