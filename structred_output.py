# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:32:34 2025

@author: Richa
"""

import os

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(api_key="insert_open_AI_Key")

#---------Step 1: Define the response format in a Pydantic model

class CalendarEvent(BaseModel):
    name: str
    date: str 
    participants: list[str]
    

# Step 2: Call the model

completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are goint to a party on Friday 18th Feb 2025."},
        ],
    response_format=CalendarEvent,

    )

# Step 3: Parse the response

event = completion.choices[0].message.parsed
event.name
event.date
event.participants
