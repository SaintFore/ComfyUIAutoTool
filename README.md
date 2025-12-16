# 🎨 ComfyUIAutoTool

ComfyUIAutoTool 是一个使用 Python 编写的命令行工具，它可以让你使用 ComfyUI 进行批量 AI 绘图。它还集成了大型语言模型（Gemini），可以根据你的想法自动生成详细的提示词。

## ✨ 主要功能

- **批量绘图**: 支持从文件中读取多个想法，并为每个想法批量生成图片。
- **智能提示词**: 使用大型语言模型（Gemini）根据你的想法自动生成详细的、高质量的提示词。
- **实时进度**: 通过 WebSocket 实时监控 ComfyUI 的绘图进度。
- **灵活配置**: 支持通过命令行参数配置 ComfyUI 服务器地址、批量大小、输出目录等。

## 🛠️ 如何使用

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 设置 API Keys

在项目根目录下创建一个 `.env` 文件，并添加你的 Google API key：

```
GOOGLE_API_KEY="your_google_api_key"
```

### 3. 准备 ComfyUI 工作流

你需要从 ComfyUI 中导出一个工作流，并将其保存为 `comfyUI.json` 文件。你可以通过在 ComfyUI 中点击 "Save (API Format)" 按钮来导出工作流。

### 4. 准备想法列表

创建一个 `idea.txt` 文件，并在其中每行输入一个你的想法（例如，“一只在月球上行走的猫”）。

### 5. 运行工具

```bash
python main.py
```

你也可以通过命令行参数来配置工具：

```bash
python main.py --ip 192.168.1.100 --batch 5 --out ./my_images
```

## ⚙️ 配置

你可以通过以下命令行参数来配置 ComfyUIAutoTool：

- `--ip`: ComfyUI 服务器的 IP 地址。
- `--batch`: 每个想法生成的图片数量。
- `--out`: 图片的输出目录。
- `--file`: 包含想法列表的文件路径。
- `--subject`: 直接输入单个想法。

## 🤝 贡献

欢迎任何形式的贡献！如果你有任何建议或问题，请随时提出 Issue。
