import os
import streamlit as st
import openai



def load_config():
    """加载并解析配置文件，返回配置对象"""
    config = configparser.ConfigParser()
    
    # 优先从项目根目录加载配置
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
    
    # 检查配置文件是否存在
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"配置文件 {config_path} 不存在")
    
    # 读取配置文件
    config.read(config_path)
    return config

def get_api_key(config):
    """从配置对象中安全获取API Key"""
    try:
        return config['API']['key']
    except (KeyError, configparser.NoSectionError) as e:
        # 记录错误但不暴露敏感信息
        print(f"配置读取错误: {e}")
        return None


# 定义你的专业背景作为上下文
context = """
我是Devin，专注于嵌入式软件开发。我有4年经验，曾参与智能家居设备开发，使用C语言和RTOS优化了低功耗性能。
我还开发过基于STM32的传感器数据采集系统，实现了I2C通信和数据实时处理。我熟练使用C/C++、RTOS、嵌入式Linux，
熟悉Keil、IAR、Git和示波器等工具。
"""

# 设置OpenAI API密钥
config = load_config()
openai.api_key = get_api_key(config)



# 定义获取AI回答的函数
def get_response(user_input):
    full_prompt = f"{context}\n\n用户问题：{user_input}\n回答："
    response = openai.Completion.create(
        model="text-davinci-003",  # 使用预训练模型
        prompt=full_prompt,
        max_tokens=150,  # 控制回答长度
        temperature=0.7  # 控制回答的创造性，0.7为平衡值
    )
    return response.choices[0].text.strip()

# 创建Streamlit界面
st.title("与Devin的AI助手对话")
st.write("我是你的AI助手，代表Devin回答关于嵌入式软件开发的问题。请告诉我您的问题！")

user_input = st.text_input("请输入您的问题：")
if user_input:
    response = get_response(user_input)
    st.write("回答：", response)