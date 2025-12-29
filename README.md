# 🎨 COMFYUI AUTO TOOL

```text
   ______                      ____  __  ______      ___         __      
  / ____/___  ____ ___  ____  / __ \/ / / /  _/     /   | __  __/ /_____ 
 / /   / __ \/ __ `__ \/ __ \/ / / / / / // /      / /| |/ / / / __/ __ \
/ /___/ /_/ / / / / / / /_/ / /_/ / /_/ // /      / ___ / /_/ / /_/ /_/ /
\____/\____/_/_/ /_/ / / .___/\___\_\____/___/     /_/  |_\__,_/\__/\____/ 
                      /_/                                               
  ______                __                                              
 /_  __/___  ____  / /                                              
  / / / __ \/ __ \/ /                                               
 / / / /_/ / /_/ / /                                                
/_/  \____/\____/_/                                                 
                                                                    
```

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-000000?style=for-the-badge&logo=comfyui&logoColor=white)](https://github.com/comfyanonymous/ComfyUI)
[![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![AI Art](https://img.shields.io/badge/Art-AI_Generation-FF69B4?style=for-the-badge)](https://github.com/SaintFore/ComfyUIAutoTool)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

**"Orchestrate your AI art factory with LLM-powered prompts."**
用 LLM 驱动的提示词，编排你的 AI 艺术工厂。

[Installation](#installation) • [Usage](#usage) • [Features](#features) • [Tech Stack](#tech-stack)

</div>

---

## ⚡ What is ComfyUIAutoTool?

**ComfyUIAutoTool** 是一个为硬核创作者打造的批量绘图自动化脚本。它打破了传统 GUI 的限制，通过 Python 调用 ComfyUI API 实现工业级吞吐。最核心的黑科技在于集成了 **Google Gemini**，能将你模糊的想法自动扩充为高质量、细节丰富的 Stable Diffusion 提示词。

**从“一个想法”到“一千张大图”，只需一次回车。**

## 🚀 Features

- **🎨 Batch Creation Engine**: 自动读取想法列表，实现无人值守的批量生图任务。
- **🧠 Gemini-Powered Prompting**: 内置 LLM 提示词增强引擎，自动补全画质词、风格描述与艺术细节。
- **📡 Real-time WebSocket Monitoring**: 实时监听服务器进度，掌握每一张图片的生成瞬间。
- **⚙️ Granular CLI Control**: 提供丰富的参数接口，支持自定义 IP、Batch Size、路径与文件。

## 📦 Installation

### 1. 克隆项目
```bash
git clone https://github.com/SaintFore/ComfyUIAutoTool.git
cd ComfyUIAutoTool
```

### 2. 安装依赖
```bash
pip install -r requirements.txt
```

### 3. 配置密钥
在 `.env` 中添加你的 Google API Key：
```env
GOOGLE_API_KEY="your_google_api_key"
```

## 💻 Usage

### 极速起航
1.  **导出工作流**: 在 ComfyUI 中点击 `Save (API Format)` 并保存为 `comfyUI.json`。
2.  **准备灵感**: 在 `idea.txt` 中每行写下一个想法。
3.  **开始作业**:
    ```bash
    python main.py --batch 4 --out ./outputs
    ```

### 进阶指令
```bash
# 指定远程服务器与单次想法
python main.py --ip 192.168.1.5 --subject "Cyberpunk neon street"
```

## 🛠️ Tech Stack

- **Engine**: Python 3.x
- **API**: ComfyUI API (WebSocket + JSON)
- **LLM**: Google Gemini Pro
- **Env**: Dotenv / Argparse

---

<div align="center">
Created with 🎨 by <a href="https://github.com/SaintFore">SaintFore</a>
</div>
