import configparser
import os
import streamlit as st
import openai
from openai import OpenAI


# 定义你的专业背景作为上下文
context = """
我是Devin，专注于嵌入式软件开发。我有4年经验，曾参与智能家居设备开发，使用C语言和RTOS优化了低功耗性能。
我还开发过基于STM32的传感器数据采集系统，实现了I2C通信和数据实时处理。我熟练使用C/C++、RTOS、嵌入式Linux，
熟悉Keil、IAR、Git和示波器等工具。
"""


# 定义获取AI回答的函数
def get_response(user_input):
    full_prompt = f"{context}\n\n用户问题：{user_input}\n回答："
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )
    return completion.choices[0].message.content


# 创建Streamlit界面
st.title("与Devin的AI助手对话")
st.write("我是你的AI助手，代表Devin回答关于嵌入式软件开发的问题。请告诉我您的问题！")

user_input = st.text_input("请输入您的问题：")
if user_input:
    response = get_response(user_input)
    st.write("回答：", response)