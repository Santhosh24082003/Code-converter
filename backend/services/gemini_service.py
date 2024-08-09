import requests
import os

# Use the correct URL for the Generative Language API
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def convert_code(cobol_code, target_language):
    headers = {
        "Content-Type": "application/json"
    }

    # Construct the prompt with COBOL code and target language
    prompt = f"Convert the following COBOL code to {target_language} and return only the converted code, without any additional formatting, explanations, or Markdown characters:\n\n{cobol_code}"

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    # Include API key in the query parameters
    url = f"{GEMINI_API_URL}?key={GEMINI_API_KEY}"

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        # Extract the converted code from the response
        converted_code = response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '').strip()
        return converted_code
    else:
        response.raise_for_status()  # Will raise an HTTPError for bad responses
