import os

class Config:
    GEMINI_API_URL = os.getenv('GEMINI_API_URL')
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
