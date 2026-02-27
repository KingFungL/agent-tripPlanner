# HelloAgents 智能旅行助手

基于 HelloAgents 多智能体框架的全栈智能旅行规划应用，支持自动生成含景点/餐饮/酒店的多日旅行行程，支持地图可视化、预算计算、行程编辑、PDF导出。

## 📋 项目架构

### 4层架构设计

1. **前端层**：Vue3 + TypeScript + Ant Design Vue + 高德地图JS API
   - 负责用户交互，收集用户需求，展示旅行计划
   - 包含行程表单、行程展示、地图渲染等核心组件

2. **后端层**：Python + FastAPI
   - 提供RESTful API接口，处理前端请求
   - 调用多智能体系统生成旅行计划
   - 数据模型定义和验证

3. **智能体层**：HelloAgents 多智能体框架
   - 景点搜索智能体：搜索目的地的景点信息
   - 天气查询智能体：查询目的地的天气信息
   - 酒店推荐智能体：推荐合适的酒店
   - 行程规划智能体：整合信息生成详细行程

4. **外部服务层**：第三方API
   - 高德地图Web API：获取地图、POI、天气等信息
   - Unsplash图片API：获取景点图片
   - LLM API：支持OpenAI/通义千问等模型

### 核心流程

```
用户输入 → 前端 → 后端API → 多智能体协作 → 外部API调用 → 行程生成 → 前端展示
```

## 📁 项目目录结构

```
├── backend/                 # 后端代码
│   ├── app/                 # 应用代码
│   │   ├── agents/          # 智能体实现
│   │   ├── api/             # API接口
│   │   ├── models/          # 数据模型
│   │   ├── services/        # 服务层
│   │   └── config.py        # 配置文件
│   ├── .env.example         # 环境变量示例
│   ├── requirements.txt     # 依赖包
│   └── run.py               # 启动脚本
├── frontend/                # 前端代码
│   ├── src/                 # 源代码
│   │   ├── services/        # API服务
│   │   ├── types/           # 类型定义
│   │   ├── views/           # 页面组件
│   │   ├── App.vue          # 根组件
│   │   └── main.ts          # 入口文件
│   ├── .env.example         # 环境变量示例
│   ├── package.json         # 依赖配置
│   └── vite.config.ts       # Vite配置
└── README.md                # 项目说明
```

## 🚀 快速开始

### 1. 环境准备

#### 后端环境

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

#### 前端环境

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install
```

### 2. API密钥申请

#### 高德地图API密钥

1. 访问 [高德开放平台](https://lbs.amap.com/)
2. 注册/登录账号
3. 创建应用，获取 Web 服务 API 密钥和 Web端(JS API) 密钥
4. 分别用于后端和前端

#### LLM API密钥

根据您选择的LLM服务提供商：
- **OpenAI**：访问 [OpenAI官网](https://platform.openai.com/) 获取API密钥
- **通义千问**：访问 [阿里云通义千问](https://tongyi.aliyun.com/) 获取API密钥

#### Unsplash API密钥（可选）

访问 [Unsplash Developer](https://unsplash.com/developers) 获取API密钥，用于获取景点图片

### 3. 配置环境变量

#### 后端配置

复制 `.env.example` 文件为 `.env`，并填写相应的API密钥：

```env
# 应用配置
APP_NAME=HelloAgents Trip Planner
APP_VERSION=1.0.0

# 服务器配置
HOST=0.0.0.0
PORT=8000

# 高德地图API配置
AMAP_MAPS_API_KEY=your_amap_web_service_key

# LLM配置
LLM_PROVIDER=openai  # 可选: openai, qwen
OPENAI_API_KEY=your_openai_api_key
QWEN_API_KEY=your_qwen_api_key

# 其他配置
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

#### 前端配置

复制 `.env.example` 文件为 `.env`，并填写相应的API密钥：

```env
# API基础URL
VITE_API_BASE_URL=http://localhost:8000

# 高德地图Web端(JS API) Key
VITE_AMAP_WEB_JS_KEY=your_amap_web_js_key
```

### 4. 启动服务

#### 启动后端

```bash
# 在backend目录下
python run.py
```

后端服务将在 `http://localhost:8000` 启动，API文档可访问 `http://localhost:8000/docs`

#### 启动前端

```bash
# 在frontend目录下
npm run dev
```

前端服务将在 `http://localhost:5173` 启动

## 🎯 核心功能

### 1. 行程规划
- 输入目的地、出行天数、偏好、预算等信息
- 系统自动生成包含景点、餐饮、酒店的详细行程
- 支持地图可视化展示

### 2. 行程编辑
- 支持调整景点顺序
- 支持删除不需要的景点
- 支持修改景点信息

### 3. 预算计算
- 自动计算景点门票、酒店住宿、餐饮费用等
- 提供详细的预算明细

### 4. 导出功能
- 支持导出为图片
- 支持导出为PDF

## 🔍 关键知识点

### 后端关键知识点

1. **Pydantic数据验证**
   - 使用Pydantic V2进行数据模型定义和验证
   - 支持字段类型检查、默认值、验证器等功能

2. **FastAPI接口开发**
   - 自动生成API文档
   - 支持异步处理
   - 内置请求验证和错误处理

3. **HelloAgents多智能体**
   - 智能体的创建和配置
   - 工具调用的实现
   - 多智能体协作流程

4. **MCP工具调用**
   - 高德地图服务的集成
   - 工具调用的格式和参数

### 前端关键知识点

1. **Vue3组合式API**
   - `setup` 语法
   - `ref` 和 `reactive` 响应式数据
   - `watch` 监听数据变化

2. **TypeScript类型定义**
   - 接口和类型定义
   - 类型约束和类型推断

3. **高德地图JS API**
   - 地图初始化和配置
   - 标记点和信息窗口
   - 路线绘制

4. **Axios网络请求**
   - 请求和响应拦截器
   - 错误处理
   - 异步请求处理

## � 个性化修改案例

### 案例1：添加景点评分字段

1. **后端修改**：在 `backend/app/models/schemas.py` 中的 `Attraction` 模型添加评分字段

2. **前端修改**：在 `frontend/src/views/Result.vue` 中显示评分信息

### 案例2：修改行程提示词

修改 `backend/app/agents/trip_planner_agent.py` 中的 `PLANNER_AGENT_PROMPT`，调整行程生成的提示词

### 案例3：更换LLM模型

在 `.env` 文件中修改 `LLM_PROVIDER` 和相应的API密钥，支持切换到不同的LLM服务

## 📖 API文档

### 核心API接口

#### POST /api/trip/plan
- **功能**：生成旅行计划
- **请求体**：
  ```json
  {
    "city": "北京",
    "start_date": "2025-06-01",
    "end_date": "2025-06-03",
    "travel_days": 3,
    "transportation": "公共交通",
    "accommodation": "经济型酒店",
    "preferences": ["历史文化", "美食"],
    "free_text_input": "希望多安排一些博物馆"
  }
  ```
- **响应**：
  ```json
  {
    "success": true,
    "message": "旅行计划生成成功",
    "data": {
      "city": "北京",
      "start_date": "2025-06-01",
      "end_date": "2025-06-03",
      "days": [...],
      "weather_info": [...],
      "overall_suggestions": "...",
      "budget": {...}
    }
  }
  ```

## � 故障排除

### 常见问题

1. **API密钥错误**：检查 `.env` 文件中的API密钥是否正确配置
2. **网络连接问题**：确保网络连接正常，LLM服务可访问
3. **端口冲突**：检查8000和5173端口是否被占用
4. **依赖包安装失败**：确保Python和Node.js版本符合要求

### 日志查看

- 后端日志：查看后端启动终端的输出
- 前端日志：查看浏览器控制台

## 🤝 贡献

欢迎提交Issue和Pull Request，共同完善这个智能旅行助手项目！

## � 许可证

MIT License

## 🎉 致谢

- [HelloAgents](https://github.com/datawhalechina/hello-agents) - 多智能体框架
- [FastAPI](https://fastapi.tiangolo.com/) - 现代Python Web框架
- [Vue3](https://vuejs.org/) - 渐进式JavaScript框架
- [Ant Design Vue](https://antdv.com/) - UI组件库
- [高德地图API](https://lbs.amap.com/) - 地图服务
- [Unsplash API](https://unsplash.com/developers) - 图片服务