from google import genai
from google.genai import types

client = genai.Client()

with open('C:\\Users\\MistrasFHR-PB2\\Desktop\\Coding\\ITEC-2905-80-Software-Development-Capstone\\Topic 7 Artificial Intelligence - Integrating AI into Python Apps\\image_understanding\\tariffs.png', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type='image/png'),
        'Make a political joke about this image?'
    ]
)

print(response.text)