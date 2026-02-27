#!/bin/bash

# 配置验证脚本
# 用于检查环境变量是否正确配置

echo "=================================="
echo "  HelloAgents 智能旅行助手"
echo "  配置验证脚本"
echo "=================================="
echo ""

# 进入后端目录
cd backend

# 检查 .env 文件是否存在
if [ ! -f ".env" ]; then
    echo "❌ .env 文件不存在"
    echo "请运行以下命令设置环境变量："
    echo "  bash setup_env.sh"
    exit 1
fi

echo "✅ .env 文件存在"
echo ""

# 检查 LLM_API_KEY
if grep -q "LLM_API_KEY=your-api-key-here" .env; then
    echo "❌ LLM_API_KEY 未配置"
    echo "   请在 .env 文件中设置 LLM_API_KEY"
else
    echo "✅ LLM_API_KEY 已配置"
fi

# 检查 LLM_BASE_URL
if grep -q "LLM_BASE_URL=your-api-base-url" .env; then
    echo "❌ LLM_BASE_URL 未配置"
    echo "   请在 .env 文件中设置 LLM_BASE_URL"
else
    echo "✅ LLM_BASE_URL 已配置"
fi

# 检查 AMAP_API_KEY
if grep -q "AMAP_API_KEY=your_amap_api_key_here" .env; then
    echo "❌ AMAP_API_KEY 未配置"
    echo "   请在 .env 文件中设置 AMAP_API_KEY"
else
    echo "✅ AMAP_API_KEY 已配置"
fi

echo ""
echo "=================================="
echo "  配置验证完成"
echo "=================================="
