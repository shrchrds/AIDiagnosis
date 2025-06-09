# Using requests library
import requests

def generate_completion():
    url = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI4MWRmYTE3OC01MWUwLTQyNzEtYTUxZC1hNzIwZTEwNTc4MDYiLCJlbWFpbCI6ImRhdGFzbmVrYXRwdXJlQGdtYWlsLmNvbSIsImlhdCI6MTc0MjE4ODIxNCwiZXhwIjoxNzczNzI0MjE0fQ.dKY-E9u1TzBx8Qorq5lxwBjBkqy1CWvybEKzD2-Si1c"
    }
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Write a poem about artificial intelligence"
            }
        ],
        "model": "gpt-4.1-nano",
        "max_tokens": 1000,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    print(data)

generate_completion()