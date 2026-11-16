LangChain-RAG 智能知识库问答系统

基于 Python 和 LangChain 构建的 RAG（Retrieval-Augmented Generation，检索增强生成）智能问答系统，支持知识库管理、文档向量化、语义检索和大模型问答。

项目以商品信息和尺码推荐为知识库示例，探索大语言模型与私有知识库结合的应用方式，减少模型幻觉，提高回答的准确性和业务相关性。

 一、项目功能

1. 知识库管理
- 支持上传知识库文件。
- 对文档进行解析和文本处理。
- 将文本转换为向量并存储。
- 支持知识库更新。

2. RAG 智能问答
- 根据用户问题进行语义检索。
- 从知识库中召回相关内容。
- 将检索结果与用户问题结合，交给大语言模型生成回答。
- 基于私有知识库提供商品信息及尺码推荐。

3. 数据管理
- 使用向量数据库存储文档向量。
- 支持知识库数据重置。
- 对文件更新及相关历史信息进行管理。

二、技术栈

| 技术 | 用途 |
|---|---|
| Python | 核心开发语言 |
| LangChain | RAG 应用开发框架 |
| Streamlit | 前端交互界面 |
| ChromaDB | 向量数据存储与检索 |
| Embedding | 文本向量化 |
| LLM API | 大语言模型调用 |

三、项目结构

```text
rag项目/
├── app_qa.py              # 智能问答界面
├── app_file_uploader.py   # 知识库文件上传
├── knowledge_base.py      # 知识库核心服务
├── vector_stores.py       # 向量存储与检索
├── file_history_store.py  # 文件历史管理
├── config_data.py         # 配置管理
├── rag.py                 # RAG 核心逻辑
├── reset_data.py          # 知识库数据重置
├── data/
│   ├── 商品信息.txt
│   └── 尺码推荐.txt
└── .gitignore
```

四、运行方式

1. 克隆项目

bash
git clone https://github.com/L923xy/-LangChain-RAG-.git
```

### 2. 进入项目目录

```bash
cd -LangChain-RAG-/rag项目
```

3. 安装依赖

建议使用 Python 虚拟环境：

```bash
python -m venv .venv
```

Windows 激活环境：

```bash
.venv\Scripts\activate
```

安装项目依赖：

```bash
pip install -r requirements.txt
```

4. 配置 API

根据项目实际使用的模型服务，在配置文件或环境变量中填写 API Key。


5. 启动项目

启动知识库管理界面：

```bash
streamlit run app_file_uploader.py
```

启动智能问答界面：

```bash
streamlit run app_qa.py
```

五、项目迭代方向

- 优化文档切分策略与 Chunk 参数。
- 优化 Embedding 模型与向量检索效果。
- 引入 Rerank 重排序机制。
- 使用 FastAPI 封装后端服务。
- 探索 LangGraph 实现多步骤 Agent 工作流。

六、项目说明

本项目为个人 AI 应用开发实践项目，持续迭代中。

GitHub：https://github.com/L923xy/-LangChain-RAG-
