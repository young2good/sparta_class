import streamlit as st
import os
from openai import OpenAI


st.title("동물 이미지 찾아주기 😍")

title = st.text_input("영어로 동물 이름을 입력해주세요", "Lion")

os.environ["OPENAI_API_KEY"] = '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'

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
