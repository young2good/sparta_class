# print("Hello World")

# ## 변수
# apple_box = 'Apple'
# print(apple_box)

# name = 'Jihye'
# print(name)

# ## 조건문
# age = 20
# if age >= 19:
#   print('성인입니다.')
# else:
#   print('청소년입니다.')

import streamlit as st
import time
from openai import OpenAI
import streamlit as st

# 코드스니펫 - 제목
st.title('[스파르타] 제품 홍보 포스터 생성기')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")
cont = '한국'

# 코드스니펫 - 버튼
if st.button('생성 :fire:'):
  with st.spinner('생성 중입니다.'):
    time.sleep(3)
    # st.write('hello')
    ## 2번 파일
    client = OpenAI(api_key=st.secrets["API_KEY"])

    chat_completion = client.chat.completions.create(
        messages=[{
            "role":
            "user",
            # "content": keyword + "라는 키워드로 제품 홍보 카피를 150자 이내로 작성해 줘",
            "content":
            f"'{cont}'에서 인기가 있을법한 '{keyword}' 라는 키워드로 제품 홍보 카피를 100자 이내의 '{cont}'언어로 작성해줘",
        }],
        model="gpt-4o",
    )

    chat_result = chat_completion.choices[0].message.content
    # print(chat_result)
    st.write(chat_result)

    ## 3번파일

    response = client.images.generate(
        model="dall-e-3",
        prompt=keyword,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    st.image(image_url)
