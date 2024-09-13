import streamlit as st
import os
from openai import OpenAI


st.title("동물 이미지 찾아주기 😍")

title = st.text_input("영어로 동물 이름을 입력해주세요", "Lion")

os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.images.generate(
  model="dall-e-3",
  prompt=f"귀여운 {title} 이미지 보여줘",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url


if st.button("Search", type="primary"):
    st.image(image_url)
else:
    st.write("")