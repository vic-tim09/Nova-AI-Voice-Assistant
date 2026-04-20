import requests
import os
from dotenv import load_dotenv

load_dotenv("API.env")
nvidia_api = os.getenv("NVIDIA_API_KEY")

def chat_with_ai(user_input):
    invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {nvidia_api}",
        "Accept": "application/json"
    }

    payload = {
        "model": "mistralai/mistral-small-4-119b-2603",
        "messages": [{"role": "user", "content": user_input}],
        "max_tokens": 200,
        "temperature": 0.5
    }

    try:
        response = requests.post(invoke_url, headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            return "AI error"

    except Exception as e:
        print(e)
        return "AI not working"