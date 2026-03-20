import os
from openai import OpenAI

# 把你的 API 密钥填在这里（注意保留引号）
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def chat_with_deepseek(user_input):
    try:
        response = client.chat.completions.create(
            model="ep-20260320125414-kqflt",
            messages=[{"role": "user", "content": user_input}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"调用失败：{str(e)}"

if __name__ == "__main__":
    print("Chatbot 已启动（输入 'exit' 退出）")
    while True:
        user_input = input("你：")
        if user_input.lower() == "exit":
            break
        reply = chat_with_deepseek(user_input)
        print(f"DeepSeek：{reply}\n")