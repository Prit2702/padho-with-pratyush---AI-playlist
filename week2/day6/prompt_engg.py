import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY is not set in .env file")

client = Groq(api_key = my_api_key)
model = "openai/gpt-oss-120b"

def llm_ans(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    return ans

bad_prompt = """
#ROLE: you are a support assistant at a mobile/laptop company
#TASK: you have to classify the issue in a category
#CONSTRAINT: you have to classify the issue in one of the three categories:
billing, technical, return
#OUTPUT FORMAT: your naswer should be only in one word only. The one word should be one of the categories in constraints.
#EXAMPLE: for instance, if a  user complain says he wants a refund then the category is return.
#FALLBACK: if the issue is unrelated to any of the categories mentionedin constraints, the n the answer should be OTHER.
This is a user complaint:
My marriage is broken.
"""
print(llm_ans(bad_prompt))