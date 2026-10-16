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

# structure is
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str
    
schema=Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}

system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema and give json object.
{schema}
"""

message_system={
    "role": "system",
    "content": system_prompt
}

text="Hello I am pritish. I broke with my girlfriend sheetal. My iphone not working, my email is prit.********@gmail.com, my address in pune. my contact no is 6767870909."

prompt=f"""
This is a  customer thicket , pls extract the personal information from this.
{text}
"""

message={
    "role":role,
    "content":prompt
}

messages = [message_system, message]
response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)

answer=response.choices[0].message.content
print(answer)

# isko padhte kese hai
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)


# Homework

# take resume in pdf or word
# have hr give you a list of things like skill, experience, projects
# extract from these resume 
# match against the hr list
# generate a percentage of matching or not
