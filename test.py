import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
workspace_id = os.getenv("WORKSPACE_ID")
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=f"https://{workspace_id}.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1",
)

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[{"role": "user", "content": "Hello, tell me about ESG reporting."}]
)
print(response.choices[0].message.content)
