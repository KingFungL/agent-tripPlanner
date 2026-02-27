"""测试LLM配置"""

from hello_agents import HelloAgentsLLM
import os
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

# 从环境变量读取配置
model = os.getenv("LLM_MODEL_ID")
api_key = os.getenv("LLM_API_KEY")
base_url = os.getenv("LLM_BASE_URL")

print(f"模型: {model}")
print(f"API密钥: {api_key[:10]}..." if api_key else "未配置")
print(f"服务地址: {base_url}")

# 测试LLM连接
try:
    llm = HelloAgentsLLM(
        model=model,
        api_key=api_key,
        base_url=base_url
    )
    print("✅ LLM初始化成功")
    
    # 测试简单的调用
    messages = [{
        "role": "user",
        "content": "你好，简单测试一下"
    }]
    
    response = llm.invoke(messages)
    print(f"✅ 调用成功")
    print(f"响应: {response.content}")
    
    if response.usage:
        print(f"Token使用量: {response.usage}")
    
    print("✅ 测试完成")
    
except Exception as e:
    print(f"❌ 测试失败: {e}")
