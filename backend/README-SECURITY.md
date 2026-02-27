# 安全配置说明

## ⚠️ 重要安全提示

**您的API密钥已经泄露！请立即采取以下措施：**

1. **立即吊销已泄露的密钥**
   - 访问阿里云百炼控制台：https://bailian.console.aliyun.com/cn-beijing/
   - 找到已泄露的API密钥
   - 点击"删除"或"禁用"按钮

2. **生成新的API密钥**
   - 在阿里云百炼控制台创建新的API密钥
   - 将新密钥保存到本地 `.env` 文件
   - **不要提交到Git仓库**

3. **更新 `.env` 文件**
   ```bash
   cd backend
   vim .env
   # 更新 LLM_API_KEY 和 AMAP_API_KEY
   ```

## 为什么需要安全配置？

### 敏感信息泄露风险

- **API密钥泄露**：可能导致您的账户被滥用，产生高额费用
- **数据泄露**：您的旅行计划、用户数据可能被窃取
- **服务滥用**：攻击者可能使用您的密钥调用API，导致服务被滥用

### 安全配置最佳实践

1. **使用环境变量存储密钥**
   - 不在代码中硬编码密钥
   - 使用 `.env` 文件存储密钥
   - 将 `.env` 添加到 `.gitignore`

2. **限制密钥访问权限**
   - 设置 `.env` 文件权限为 `600`（仅所有者可读写）
   - 不要在公共场合分享 `.env` 文件

3. **定期轮换密钥**
   - 定期生成新的API密钥
   - 更新 `.env` 文件
   - 重启服务

4. **使用密钥管理服务**
   - 推荐使用阿里云KMS（密钥管理服务）
   - 或使用其他专业的密钥管理工具

## 项目安全配置

### 1. 环境变量配置

项目使用 `.env` 文件存储敏感信息：

```env
# LLM配置
LLM_API_KEY=sk-您的实际密钥
LLM_BASE_URL=https://ark.cn-beijing.volces.com/api/v3

# 高德地图API配置
AMAP_API_KEY=您的高德地图密钥
```

### 2. Git配置

`.gitignore` 文件已经配置忽略 `.env` 文件：

```gitignore
# 环境变量
.env
.env.local
```

### 3. 配置验证

项目实现了配置验证功能，启动时会自动检查必要配置：

```python
from app.config import validate_config

# 验证配置
validate_config()  # 如果配置缺失会抛出异常
```

### 4. 敏感信息隐藏

配置模块已经实现了敏感信息隐藏功能，日志中不会显示完整密钥：

```python
from app.config import print_config

print_config()  # 只显示密钥的前10位和后4位
# 输出示例：LLM API Key: sk-3d3466fae...6bd0
```

## 快速开始

### 1. 运行设置脚本

```bash
cd backend
bash setup_env.sh
```

### 2. 编辑 `.env` 文件

```bash
vim .env
```

填入您的密钥。

### 3. 验证配置

```bash
bash verify_config.sh
```

### 4. 启动服务

```bash
bash start.sh
```

## 配置文件说明

| 文件 | 说明 | 是否提交到Git |
|------|------|---------------|
| `.env` | 环境变量配置（包含密钥） | ❌ 不提交 |
| `.env.example` | 环境变量示例（不包含密钥） | ✅ 提交 |
| `SECURITY.md` | 安全配置指南 | ✅ 提交 |
| `QUICKSTART.md` | 快速开始指南 | ✅ 提交 |

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

## 相关资源

- [阿里云百炼控制台](https://bailian.console.aliyun.com/cn-beijing/)
- [阿里云百炼文档](https://help.aliyun.com/zh/model-studio/)
- [API参考](https://help.aliyun.com/zh/model-studio/developer-reference)
- [Git安全最佳实践](https://docs.github.com/en/repositories/working-with-files/using-files/recommending-repository-settings)

## 联系支持

如果您遇到任何安全问题，请联系：
- 阿里云技术支持：https://help.aliyun.com/
- 高德地图技术支持：https://lbs.amap.com/
