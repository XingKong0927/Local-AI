"""
环境：ai_1
Created on Sun Jun 11 16:58:05 2023"""

# -*- coding: utf-8 -*-

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='deepseek-r1:7b', messages=[
  {
    'role': 'user',
    'content': '你还记我问过什么吗？',
  },
])
# print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)
