import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key= os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("what is you name" , stream= False)

# reply = []

# for chunks in response.text:
#     reply.append(chunks)

print(response.text)