import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key= my_api_key )

model="llama-3.3-70b-versatile"
role="user"
text = "Hello mu name is harsh i bought a iphone from your store .It stop wroking please contanct me on abc@gmail.com. My contact is 45989"
prompt=f""" 
        This is customer details please extract the personal information from this {text} """
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message]


response=client.chat.completions.create(model=model, messages=messages)


answer = response.choices[0].message.content
print(answer)