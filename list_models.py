import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

models = client.models.list()

print("AVAILABLE MODELS:\n")

for model in models.data:
    print(model.id)

