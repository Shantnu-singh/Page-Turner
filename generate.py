import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("what is you name" , stream= False)

# reply = []

def get_gemini_response(prompt, context=""):
    try:
        full_prompt = f"Context: {context}\n\nQuestion: {prompt}\n\nPlease answer based on the context provided."
        response = model.generate_content(full_prompt, stream=False)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

# print(response.text)