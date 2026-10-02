import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

def openrouter_client(prompt, model="gpt-4o-mini", sys_msg=None):
    if not api_key:
        raise ValueError("API_KEY not set in environment variables.")
    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )

    completion = client.chat.completions.create(
        model="openrouter/gpt-4o-mini",
        messages=[
            {"role":"system", "content": prompt},
            {"role":"user", "content": "write a poem about the ocean."}
        ]
    )
    return completion.choices[0].message.content









    

