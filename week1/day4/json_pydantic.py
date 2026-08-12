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

# Structure format 
from pydantic import BaseModel
class Ticket(BaseModel):
    name : str
    email : str 
    issue : str 
schema = Ticket.model_json_schema()
response_format = {
    "type" : "json_object"
}
system_prompt = f"""
Extract the personal information from the ticket stricly on this schema and give json output{schema}"""

message_system = {
    "role" : "system",
    "content" : system_prompt
}


text = "Hello my name is harsh i bought a iphone from your store .It stop wroking please contanct me on abc@gmail.com. My contact is 45989"
prompt=f""" 
        This is customer details please extract the personal information from this {text} """
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system,message]


response=client.chat.completions.create(model=model, messages=messages, response_format = response_format)


answer = response.choices[0].message.content
print(answer)

# isko padhta kasa hai 
import json 
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)


print(ticket.name)
print(ticket.email)
print(ticket.issue)