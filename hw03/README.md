
markdown
# 人脸检测与识别系统（hw03）

## 项目结构
hw03/
├── app.py # Streamlit 主界面
├── requirements.txt # Python 依赖
├── README.md # 项目说明
├── src/
│ └── face_utils.py # 人脸检测与识别核心逻辑
├── known_faces/ # 已知人脸库（需手动添加图片）
└── examples/ # 示例图片（可选）

text

## 功能说明
- **人脸检测**：使用 `face_recognition` 库检测图片中所有人脸的位置。
- **人脸编码**：为每张人脸生成 128 维特征向量。
- **人脸识别**：将检测到的人脸与已知人脸库比对，输出最匹配的人名（或“未知”）。
- **Web 界面**：基于 Streamlit 提供上传图片或选择示例图的功能，并可视化检测结果。

## 环境准备
1. Python 3.8 或更高版本。
2. 安装系统依赖（用于 dlib）：
   - Windows：安装 Visual C++ Build Tools
   - macOS：安装 Xcode Command Line Tools
   - Linux：`sudo apt install build-essential cmake libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev`
3. 创建虚拟环境并安装依赖：
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
运行方式
在项目根目录下执行：

bash
streamlit run app.py
浏览器将自动打开 http://localhost:8501，即可使用。

使用说明
上传图片：点击“浏览文件”选择本地图片。

选择示例：从侧边栏选择预置示例图片。

系统会自动检测人脸并在图片上标注框和姓名，下方显示识别结果。

已知人脸库
将需要识别的人脸图片放入 known_faces/ 目录，文件名即为对应的人名（如 zhang_san.jpg）。程序启动时会自动加载这些图片并计算特征向量。

注意事项
如果识别结果全是“未知”，请检查人脸库图片质量（建议正面、清晰、单张脸）。

中文标签显示可能需要调整字体，可改用英文名避免字体问题。

text
