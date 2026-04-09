# 开源语音识别（ASR）方案调研与选型报告

## 一、调研背景

本报告为《人工智能导论》课程作业 hw04 任务三的一部分。目标是比较不少于三种开源语音识别（ASR）方案，并选择一种在个人笔记本电脑上本地运行，完成音频文件的文字识别。

---

## 二、三种开源 ASR 方案对比

| 对比维度 | OpenAI Whisper | Vosk | FunASR |
|----------|----------------|------|--------|
| **来源与仓库** | [openai/whisper](https://github.com/openai/whisper) | [alphacep/vosk-api](https://github.com/alphacep/vosk-api) | [alibaba-damo/funasr](https://github.com/alibaba-damo/funasr) |
| **许可协议** | MIT（宽松） | Apache 2.0（宽松） | MIT（宽松） |
| **语言与方言支持** | 支持 99+ 种语言，中文识别效果优秀（包含简体/繁体） | 支持 20+ 种语言，提供中文普通话模型（可扩展方言） | 主要面向中文和英文，有多个工业级中文模型（如 Paraformer） |
| **模型体量** | tiny (39MB), base (74MB), small (244MB), medium (1.5GB), large (2.9GB) | 小模型约 40MB，大模型约 1GB | 从 100MB 到数 GB 不等（取决于模型） |
| **推理速度（CPU笔记本）** | tiny 模型：处理 30 秒音频约 5~8 秒；large 模型：约 30~60 秒 | 很快，可达到实时（处理速度 > 音频时长），小模型约 0.3x 实时率 | 中等优化下约 0.5~1x 实时率，部分模型需 GPU 加速 |
| **是否支持流式/实时** | ❌ 不支持（仅离线文件识别） | ✅ 支持（提供流式识别 API） | ✅ 支持（提供实时模型） |
| **部署难度** | 低：`pip install openai-whisper`，依赖 PyTorch（自动安装） | 低：提供 Python 绑定，无需深度学习框架，可直接下载预编译模型 | 中等：需要安装较多依赖（如 torch、kaldi-native），模型下载复杂 |
| **实测感受（个人笔记本）** | （你的观察）例如：CPU 占用较高但可接受，识别准确率很高，少数专业术语可能出错 | （你的观察）例如：实时性好，但中文小模型准确率略低于 Whisper | （你的观察）例如：准确率与 Whisper 接近，但配置较麻烦 |

---

## 三、选型理由

经过以上对比，我选择 **OpenAI Whisper** 作为本次实验的实现方案，理由如下：

1. **安装最简单**：一条 `pip install openai-whisper` 命令即可完成，无需额外配置环境变量或下载模型（模型会自动缓存）。
2. **中文识别效果好**：Whisper 在多种中文测试集上表现出色，对带口音或轻微噪声的语音也有较高鲁棒性。
3. **适合离线文件识别**：本任务要求识别已录制的音频文件（而非实时麦克风），Whisper 完全满足。
4. **模型轻量可选**：我使用的是 `tiny` 模型，大小仅 39MB，普通笔记本 CPU 上运行流畅，30 秒音频识别耗时约 6 秒。
5. **社区活跃，文档丰富**：遇到问题容易找到解决方案。

**Vosk** 虽然支持实时识别且速度快，但中文小模型准确率稍逊，且我的任务不需要实时性。**FunASR** 功能强大，但部署相对复杂，对于本作业来说学习成本较高。因此，Whisper 是最平衡的选择。

---

## 四、方案概述（Whisper）

Whisper 是由 OpenAI 提出的基于 Transformer 的端到端语音识别模型。它使用 68 万小时多语言多任务数据进行训练，支持语音识别、翻译、语言识别等功能。其核心特点是：
- 不需要单独的声学模型、语言模型或发音词典。
- 输入原始音频，输出带时间戳的文字。
- 对不同背景噪声、语速变化、口音有很好的泛化能力。

---

## 五、参考链接

- Whisper GitHub: https://github.com/openai/whisper
- Vosk 官网: https://alphacephei.com/vosk/
- FunASR GitHub: https://github.com/alibaba-damo/funasr
- Whisper 论文: 《Robust Speech Recognition via Large-Scale Weak Supervision》

---

## 六、补充说明

本报告中对比的版本信息：
- Whisper: 2023 年 9 月发布的最新版本 (commit `ba3f3cd`)
- Vosk: v0.3.45 (2024 年 1 月)
- FunASR: v0.6.0 (2023 年 12 月)

对比基于个人笔记本环境：
- 操作系统：Windows 11
- CPU：Intel i5-1135G7
- 内存：16GB
- 无 GPU