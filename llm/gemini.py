import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

completion = client.chat.completions.create(
    model="openrouter/gpt-4o-mini",
    messages=[
        {"role":"system", "content": "you are a helpful assistant."},
        {"role":"user", "content": "write a poem about the ocean."}
    ]
)
print(completion.choices[0].message.content)







    

