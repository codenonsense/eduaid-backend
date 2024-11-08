import google.generativeai as generativeai
from config import GEMINI_API_KEY


generativeai.configure(api_key=GEMINI_API_KEY)
model = generativeai.GenerativeModel(model_name='gemini-1.5-flash')

def get_chat_text(prompt):
    response = model.generate_content(prompt)
    return response
