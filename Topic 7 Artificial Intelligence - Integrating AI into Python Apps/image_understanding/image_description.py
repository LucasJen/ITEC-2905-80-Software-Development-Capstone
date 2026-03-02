from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel

client = genai.Client()

class Produce(BaseModel):
    name: str
    color: str
    fruit_or_veg: str

with open('hilux.jpeg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type='image/png'),
        'what trucks is this a picture of?'
    ],
    config=GenerateContentConfig(
        system_instruction="""
            pretend these trucks are actually in the produce isle, tell me which one's look more like a fruit and other a vegetable.
        """,
        response_mime_type='application/json',
        response_schema=list[Produce]
    )
)

print(response.parsed)

for produce_item in response.parsed:
    print(produce_item.name)
