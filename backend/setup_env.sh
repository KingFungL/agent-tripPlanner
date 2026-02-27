#!/bin/bash

# 安全配置设置脚本
# 用于快速设置后端环境变量

echo "=================================="
echo "  HelloAgents 智能旅行助手"
echo "  环境变量设置脚本"
echo "=================================="
echo ""

# 进入后端目录
cd backend

# 检查 .env 文件是否存在
if [ -f ".env" ]; then
    echo "⚠️  .env 文件已存在"
    read -p "是否覆盖？(y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "操作已取消"
        exit 1
    fi
fi

# 复制 .env.example 文件
cp .env.example .env
echo "✅ 已创建 .env 文件"

# 提示用户编辑 .env 文件
echo ""
echo "=================================="
echo "  请编辑 .env 文件，填入您的密钥"
echo "=================================="
echo ""
echo "需要配置的密钥："
echo "  1. LLM_API_KEY - 阿里云百炼API密钥"
echo "  2. LLM_BASE_URL - 服务地址（默认：https://ark.cn-beijing.volces.com/api/v3）"
echo "  3. AMAP_API_KEY - 高德地图API密钥"
echo ""
echo "配置完成后，运行以下命令启动服务："
echo "  python3 run.py"
echo ""
echo "详细配置说明请参考：backend/SECURITY.md"
