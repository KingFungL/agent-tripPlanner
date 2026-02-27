# 安全配置指南

## 重要提示

**您的API密钥已经泄露！请立即采取以下措施：**

1. **立即吊销已泄露的密钥**
   - 访问阿里云百炼控制台：https://bailian.console.aliyun.com/cn-beijing/
   - 找到已泄露的API密钥
   - 点击"删除"或"禁用"按钮

2. **生成新的API密钥**
   - 在阿里云百炼控制台创建新的API密钥
   - 复制新密钥，但不要提交到代码仓库

## 安全配置最佳实践

### 1. 环境变量配置

项目已经配置了 `.gitignore` 文件，确保 `.env` 文件不会被提交到Git仓库：

```bash
# .gitignore 中已包含
.env
.env.local
```

### 2. 安全的配置管理

#### 创建 `.env` 文件（本地使用）

```bash
cd backend
cp .env.example .env
```

编辑 `.env` 文件，填入您的密钥：

```env
# LLM配置
LLM_MODEL_ID=qwen-turbo
LLM_API_KEY=sk-您的实际密钥
LLM_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
LLM_TIMEOUT=60

# 高德地图API配置
AMAP_API_KEY=您的高德地图密钥

# 服务器配置
HOST=0.0.0.0
PORT=8000

# CORS配置
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# 日志级别
LOG_LEVEL=INFO
```

#### 创建 `.env.example` 文件（提交到Git）

`.env.example` 文件应该包含示例配置，不包含真实密钥：

```env
# LLM配置
LLM_MODEL_ID=qwen-turbo
LLM_API_KEY=your-api-key-here
LLM_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
LLM_TIMEOUT=60

# 高德地图API配置
AMAP_API_KEY=your-amap-api-key-here

# 服务器配置
HOST=0.0.0.0
PORT=8000

# CORS配置
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# 日志级别
LOG_LEVEL=INFO
```

### 3. 配置验证

项目已经实现了配置验证功能，启动时会自动检查必要配置：

```python
from app.config import validate_config

# 验证配置
validate_config()  # 如果配置缺失会抛出异常
```

### 4. 敏感信息隐藏

配置模块已经实现了敏感信息隐藏功能，日志中不会显示完整密钥：

```python
from app.config import get_settings, print_config

settings = get_settings()
print_config()  # 只显示密钥的前10位和后4位
```

## 阿里云百炼API密钥配置

### 1. 登录阿里云百炼控制台

访问：https://bailian.console.aliyun.com/cn-beijing/

### 2. 创建API密钥

1. 在控制台找到"API密钥"或"密钥管理"选项
2. 点击"创建密钥"
3. 复制生成的密钥（只显示一次）
4. 将密钥保存到 `.env` 文件

### 3. 配置服务地址

对于阿里云百炼的千问模型，服务地址为：

```env
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
```

或者：

```env
LLM_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
```

### 4. 测试配置

创建测试脚本 `test_config.py`：

```python
import os
from dotenv import load_dotenv

load_dotenv()

# 检查配置
print("LLM_API_KEY:", os.getenv("LLM_API_KEY")[:10] + "..." if os.getenv("LLM_API_KEY") else "未配置")
print("LLM_BASE_URL:", os.getenv("LLM_BASE_URL"))
print("AMAP_API_KEY:", os.getenv("AMAP_API_KEY")[:10] + "..." if os.getenv("AMAP_API_KEY") else "未配置")
```

运行测试：

```bash
cd backend
python3 test_config.py
```

## 安全检查清单

- [ ] 已吊销已泄露的API密钥
- [ ] 已生成新的API密钥
- [ ] `.env` 文件已添加到 `.gitignore`
- [ ] `.env.example` 文件包含示例配置
- [ ] 所有密钥都存储在 `.env` 文件中
- [ ] 不在代码中硬编码密钥
- [ ] 不在日志中输出完整密钥
- [ ] 定期轮换API密钥
- [ ] 限制 `.env` 文件的访问权限（chmod 600）

## 常见安全问题

### 1. 密钥泄露怎么办？

- 立即吊销泄露的密钥
- 生成新的密钥
- 更新 `.env` 文件
- 重启服务

### 2. 如何防止密钥泄露？

- 使用环境变量存储密钥
- 将 `.env` 添加到 `.gitignore`
- 不在代码中硬编码密钥
- 不在日志中输出密钥
- 使用密钥管理服务（如阿里云KMS）

### 3. 如何安全地分享项目？

- 提供 `.env.example` 文件
- 在文档中说明需要配置哪些密钥
- 不提交包含真实密钥的 `.env` 文件

## 阿里云百炼相关资源

- 控制台：https://bailian.console.aliyun.com/cn-beijing/
- 文档：https://help.aliyun.com/zh/model-studio/
- API参考：https://help.aliyun.com/zh/model-studio/developer-reference
