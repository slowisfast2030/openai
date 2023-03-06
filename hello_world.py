# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
openai.api_key = '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'

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "shell脚本读取文件，一行行输出。给出行号，行号右对齐。"}
    ]
)

#print(response)
print(response['choices'][0]['message']['content'])
