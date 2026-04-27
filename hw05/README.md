markdown

\# hw05 - 卷积神经网络实验



本目录包含两个在 MNIST 手写数字数据集上训练的 CNN 模型：极简 CNN 与 LeNet-5。



\## 目录结构

hw05/

├── README.md # 本文件

├── report.md # 实验报告

├── debug\_notes.md # 调试记录

├── requirements.txt # Python 依赖

├── simple\_cnn/

│ └── train\_simple\_cnn.py # 极简 CNN 训练脚本（来源：公众号《计算机视觉》第10篇）

└── lenet5/

├── model.py # LeNet-5 模型定义

└── train\_lenet5.py # LeNet-5 训练脚本



text



\## 环境要求



\- Python 3.9+

\- 依赖见 `requirements.txt`



\## 安装与运行



1\. 安装依赖（建议在虚拟环境中）：

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

训练极简 CNN：



bash

cd simple\_cnn

python train\_simple\_cnn.py

测试准确率将打印在终端，模型保存为 simple\_cnn\_mnist.pth。



训练 LeNet-5：



bash

cd lenet5

python train\_lenet5.py

训练结束后将输出测试准确率、训练时间和参数量，模型保存为 lenet5\_mnist.pth。



数据说明：



两个脚本均会自动下载 MNIST 数据集至各自的 ./data 文件夹。若网络不佳，可手动下载后放置于 data/MNIST/raw/，并将代码中 download=True 改为 False。



极简 CNN 代码会生成若干图片（mnist\_samples.png、predictions.png、training\_loss.png），属于可选的可视化输出。



实验结果摘要

模型	测试准确率	参数量	训练时间

极简 CNN	98.18%	31,530	\~150 秒

LeNet-5	98.96%	44,426	460.71 秒

