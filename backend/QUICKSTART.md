# 快速开始指南

## 1. 安全配置设置

### 第一步：运行设置脚本

```bash
cd backend
bash setup_env.sh
```

这会创建一个 `.env` 文件，您需要编辑它来填入您的密钥。

### 第二步：编辑 `.env` 文件

```bash
vim .env
# 或者
nano .env
```

填入您的密钥：

```env
# LLM配置
LLM_MODEL_ID=qwen-turbo
LLM_API_KEY=sk-您的实际密钥
LLM_BASE_URL=https://ark.cn-beijing.volces.com/api/v3
LLM_TIMEOUT=60

# 高德地图API配置
AMAP_API_KEY=您的高德地图密钥
```

### 第三步：验证配置

```bash
bash verify_config.sh
```

## 2. 启动服务

### 方式一：使用启动脚本

```bash
bash start.sh
```

### 方式二：手动启动

```bash
python3 run.py
```

## 3. 访问服务

启动成功后，您可以通过以下地址访问服务：

- **服务地址**: http://localhost:8000
- **API文档**: http://localhost:8000/docs
- **健康检查**: http://localhost:8000/health

## 4. 配置说明

### LLM配置

- **LLM_MODEL_ID**: 模型名称，如 `qwen-turbo`
- **LLM_API_KEY**: API密钥（必填）
- **LLM_BASE_URL**: 服务地址（必填）
  - 阿里云百炼: `https://dashscope.aliyuncs.com/compatible-mode/v1`
  - 火山引擎Ark: `https://ark.cn-beijing.volces.com/api/v3`
- **LLM_TIMEOUT**: 超时时间（秒），默认60

### 高德地图API配置

- **AMAP_API_KEY**: 高德地图API密钥（必填）

### 服务器配置

- **HOST**: 服务器地址，默认 `0.0.0.0`
- **PORT**: 服务器端口，默认 `8000`
- **CORS_ORIGINS**: CORS允许的源，默认 `http://localhost:5173,http://localhost:3000`
- **LOG_LEVEL**: 日志级别，默认 `INFO`

## 5. 常见问题

### Q: 如何获取阿里云百炼API密钥？

A: 访问 https://bailian.console.aliyun.com/cn-beijing/，登录后在控制台创建API密钥。

### Q: 如何获取高德地图API密钥？

A: 访问 https://lbs.amap.com/，注册后创建应用并获取API密钥。

### Q: 服务启动失败怎么办？

A: 检查以下几点：
1. `.env` 文件是否存在
2. 所有必填配置是否已填写
3. API密钥是否正确
4. 网络连接是否正常

### Q: 如何查看日志？

A: 启动服务时会输出日志到控制台。您也可以查看 `.log` 文件（如果配置了日志文件输出）。

## 6. 安全建议

1. **不要将 `.env` 文件提交到Git仓库**
   - `.gitignore` 已经配置忽略 `.env` 文件
   - 确保不要手动添加 `.env` 到Git

2. **定期轮换API密钥**
   - 定期生成新的API密钥
   - 更新 `.env` 文件
   - 重启服务

3. **限制 `.env` 文件的访问权限**
   ```bash
   chmod 600 .env
   ```

4. **使用环境变量管理工具**
   - 推荐使用 `dotenv` 或 `envdir`
   - 不要在代码中硬编码密钥

5. **不要在日志中输出密钥**
   - 配置模块已经实现了密钥隐藏功能
   - 日志中只会显示密钥的前10位和后4位

## 7. 相关文档

- [安全配置指南](SECURITY.md) - 详细的安全配置说明
- [API文档](http://localhost:8000/docs) - 启动服务后可访问
