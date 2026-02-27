#!/usr/bin/env python3
"""配置安全检查脚本"""

import os
import sys
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def check_config():
    """检查配置是否安全"""
    print("=" * 60)
    print("  HelloAgents 智能旅行助手")
    print("  配置安全检查")
    print("=" * 60)
    print()
    
    errors = []
    warnings = []
    
    # 检查 .env 文件
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        print("✅ .env 文件存在")
    else:
        print("❌ .env 文件不存在")
        errors.append(".env 文件不存在")
    
    # 检查 LLM_API_KEY
    llm_api_key = os.getenv("LLM_API_KEY", "")
    if not llm_api_key or llm_api_key == "your-api-key-here":
        print("❌ LLM_API_KEY 未配置")
        errors.append("LLM_API_KEY 未配置")
    else:
        print("✅ LLM_API_KEY 已配置")
        # 检查密钥长度
        if len(llm_api_key) < 10:
            print("⚠️  LLM_API_KEY 长度异常")
            warnings.append("LLM_API_KEY 长度异常")
    
    # 检查 LLM_BASE_URL
    llm_base_url = os.getenv("LLM_BASE_URL", "")
    if not llm_base_url or llm_base_url == "your-api-base-url":
        print("❌ LLM_BASE_URL 未配置")
        errors.append("LLM_BASE_URL 未配置")
    else:
        print("✅ LLM_BASE_URL 已配置")
    
    # 检查 AMAP_API_KEY
    amap_api_key = os.getenv("AMAP_API_KEY", "")
    if not amap_api_key or amap_api_key == "your_amap_api_key_here":
        print("❌ AMAP_API_KEY 未配置")
        errors.append("AMAP_API_KEY 未配置")
    else:
        print("✅ AMAP_API_KEY 已配置")
    
    # 检查敏感信息隐藏
    print()
    print("敏感信息隐藏测试：")
    if llm_api_key:
        masked_key = f"{llm_api_key[:10]}...{llm_api_key[-4:] if len(llm_api_key) > 14 else ''}"
        print(f"  LLM_API_KEY: {masked_key}")
    if amap_api_key:
        masked_key = f"{amap_api_key[:10]}...{amap_api_key[-4:] if len(amap_api_key) > 14 else ''}"
        print(f"  AMAP_API_KEY: {masked_key}")
    
    # 检查 .gitignore
    print()
    print("Git配置检查：")
    gitignore_path = os.path.join(os.path.dirname(__file__), "..", ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            gitignore_content = f.read()
            if ".env" in gitignore_content:
                print("✅ .gitignore 已配置忽略 .env 文件")
            else:
                print("❌ .gitignore 未配置忽略 .env 文件")
                errors.append(".gitignore 未配置忽略 .env 文件")
    else:
        print("❌ .gitignore 文件不存在")
        errors.append(".gitignore 文件不存在")
    
    # 输出结果
    print()
    print("=" * 60)
    if errors:
        print("❌ 配置检查失败")
        print()
        print("错误：")
        for error in errors:
            print(f"  - {error}")
        print()
        print("请修复上述问题后再启动服务")
        return False
    elif warnings:
        print("⚠️  配置检查通过，但有警告")
        print()
        print("警告：")
        for warning in warnings:
            print(f"  - {warning}")
        return True
    else:
        print("✅ 配置检查通过")
        return True

if __name__ == "__main__":
    success = check_config()
    sys.exit(0 if success else 1)
