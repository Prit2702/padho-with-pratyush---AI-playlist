import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in .env file")

client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-20b"
role = "user"
prompt = "Provide me name for my food company"
#  System
message_system={
    "role":"system",
    "content":"You are a brand maanger who suggest name for my food brand. Just answer in less than 5 word only, suggest one name only."
}

message={
    "role":role,
    "content":prompt
}

messages = [message_system, message]
# Temperature [0-2]
response = client.chat.completions.create(model=model, messages=messages, temperature=2)

answer=response.choices[0].message.content
print(answer)



