from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="""We are a business selling loggin and monitoring products, what are good products give away at our booth at Pycon? Last year we
    gave away tote bags and those worked well and stayed within budget"""
    
)

print(response.text)