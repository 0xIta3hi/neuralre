import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def openrouter_client(prompt, model="openai/gpt-4o-mini", sys_msg=None):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY is not set in the environment.")

    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )

    completion = client.chat.completions.create(
        model=model,
        messages=(
            ([{"role": "system", "content": sys_msg}] if sys_msg else [])
            + [{"role": "user", "content": prompt}]
        ),
    )
    return completion.choices[0].message.content

