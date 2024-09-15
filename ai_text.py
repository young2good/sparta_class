import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']

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