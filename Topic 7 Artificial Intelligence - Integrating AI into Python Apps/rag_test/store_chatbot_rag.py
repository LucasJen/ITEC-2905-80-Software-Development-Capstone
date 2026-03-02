from google import genai
from google.genai import types
from google.genai.types import GenerateContentConfig
import rich
from rich.markdown import Markdown
import sys
import os
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
import pandas


class GeminiEmbeddingFunction(EmbeddingFunction):
    document_mode = True # True = generating embeddings, False = searching for embeddings in the db

    def __call__(self, input: Documents):
        if self.document_mode:
            embedding_task = 'retrieval_document'
        else:
            embedding_task = 'retrieval_query'
        
        response = client.models.embed_content(
            model='models/text-embedding-004',
            contents=input,
            config=types.EmbeddingContentConfig(
                task_type=embedding_task
            )
        )

        return [e.values for e in response.embeddings] #list comprehension.

embed_function = GeminiEmbeddingFunction()
embed_function.document_mode = True

chroma_client = chromadb.PersistentClient()
db = chroma_client.get_or_create_collection(name='zoomies_clothes', embedding_function=embed_function)

with open('fitness_clothing_descriptions', 'r') as file:
    clothing_data = pandas.read_csv(file)
    ids = list(clothing_data.style_code)
    documents = list(clothing_data.description)

db.upsert(
    ids=ids,
    documents=documents
)

embed_function.document_mode = False # querying the database - find relevant documents

query = 'What are the best pants?'
result = db.query(query_texts=[query], n_results=5) # how many results to return?
[all_items] = result['documents']
print(all_items)

client = genai.Client()
chat = client.chats.create(model='gemini-2.5-flash')

try:
    with open('chat_system_instructions.txt', 'r') as f:
        system_instructions_text = f.read()
except:
    print('missing system instruction, quitting.')
    sys.exit()

while True:
    question = input('> ')
    response = chat.send_message(
        # model='gemini-2.5-flash',
        question,
        config=GenerateContentConfig(
            system_instruction=system_instructions_text
        )
    )

    rich.print(Markdown(response.text))