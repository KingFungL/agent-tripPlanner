#!/bin/bash

# 快速启动脚本
# 用于快速启动后端服务

echo "=================================="
echo "  HelloAgents 智能旅行助手"
echo "  启动脚本"
echo "=================================="
echo ""

# 进入后端目录
cd backend

# 检查 .env 文件是否存在
if [ ! -f ".env" ]; then
    echo "❌ .env 文件不存在"
    echo "请先运行以下命令设置环境变量："
    echo "  bash setup_env.sh"
    exit 1
fi

# 验证配置
echo "正在验证配置..."
bash verify_config.sh
echo ""

# 检查配置是否通过
if ! grep -q "配置验证完成" < <(bash verify_config.sh); then
    echo "❌ 配置验证未通过，请先修复配置问题"
    exit 1
fi

echo "✅ 配置验证通过"
echo ""

# 启动服务
echo "正在启动服务..."
echo "服务地址: http://localhost:8000"
echo "API文档: http://localhost:8000/docs"
echo ""
python3 run.py
