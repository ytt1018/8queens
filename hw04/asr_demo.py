import whisper

# 加载 tiny 模型
model = whisper.load_model("tiny")

# 指定音频文件（确保文件名与你的实际音频一致）
audio_file = "my_voice_tts.mp3"   # 如果你用的是其他名字，请改成实际文件名

# 识别（指定中文）
print("正在识别，请稍等...")
result = model.transcribe(audio_file, language="zh")

# 输出结果
print("\n识别结果：")
print(result["text"])

# 保存结果到文件
with open("recognition_output.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("\n结果已保存到 recognition_output.txt")