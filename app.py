
import streamlit as st
import time
import os
from openai import OpenAI
import streamlit as st

#setting 값
os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

# 코드스니펫 - 제목
st.title('캐치프레이즈 작성기:sunny:')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")
# cont = '한국'

if st.button('생성 :fire:'):
    with st.spinner('Wait for it...'):
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
    result = chat_completion.choices[0].message.content
    st.write(result)



# # 코드스니펫 - 버튼
# if st.button('생성 :fire:'):
#   with st.spinner('생성 중입니다.'):
#     time.sleep(3)
#     # st.write('hello')
#     ## 2번 파일
#     client = OpenAI(api_key=st.secrets["api"]["API_KEY"])

#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role":"user",
#                 "content": keyword,
#             },
#             {
#                 "role":"system",
#                 "content": "입력받은 키워드에 대한 캐치프레이즈를 100자이내로 작성해줘",
#             }
#         ],
#         model="gpt-4o",
#     )

#     chat_result = chat_completion.choices[0].message.content
#     # print(chat_result)
#     st.write(chat_result)

#     ## 3번파일

#     response = client.images.generate(
#         model="dall-e-3",
#         prompt=keyword,
#         size="1024x1024",
#         quality="standard",
#         n=1,
#     )

#     image_url = response.data[0].url
#     st.image(image_url)
