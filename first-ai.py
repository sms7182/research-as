import requests

RUNPOD_API_URL = "https://api.runpod.ai/v1/your-model-id/generate"


API_KEY = "your-runpod-api-key"

input_data = {
    "input": {
        "prompt": "میخوام پیتزا درست کنم",  
        "max_tokens": 100,  
        "temperature": 0.7  
    }
}

headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.post(RUNPOD_API_URL, json=input_data, headers=headers)

if response.status_code == 200:
    ai_response = response.json()
    print("AI Response:", ai_response['output'])
else:
    print("Error:", response.status_code, response.text)