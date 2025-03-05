# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 17:08:10 2025
Code from @daveebbelaar
@author: Richa
"""

import os

from openai import OpenAI

client = OpenAI(api_key="insert_open_AI_Key")

completion = client.chat.completions.create(
    model ="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {
            "role":"user",
            "content":"write a limerick about python programming language."
            },
        ],
    )

response = completion.choices[0].message.content
print(response)


