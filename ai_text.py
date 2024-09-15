import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "치킨",
        },
        {
            "role": "system",
            "content": "입력받은 키워드에 대한 캐치프레이즈를 100자이내로 작성해줘",
        }
    ],
    model="gpt-4o",
)

print(chat_completion.choices[0].message.content)