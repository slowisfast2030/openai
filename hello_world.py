# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

print(openai.api_key)
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "写一个二叉树遍历脚本"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])
