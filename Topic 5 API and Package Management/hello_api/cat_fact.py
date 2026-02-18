import requests

response = requests.get('https://catfact.ninja/fact')
print(response.status_code)

# response.raise_for_status
print(response.text)
print(response.json())

data= response.json()

fact = data['fact']
print(f'A random cat fact: {fact}')