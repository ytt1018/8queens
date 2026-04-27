"""
极简卷积神经网络 CNN 识别手写数字
来源：《计算机视觉》第10篇（微信公众号：人工智能科技前沿）
链接：https://mp.weixin.qq.com/s/iBNvhk-uAeAfTuanxiLs9Q
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np


# ---------- 4.2 定义CNN模型 ----------
class SimpleCNN(nn.Module):
    """简单的卷积神经网络模型，用于MNIST手写数字分类
    结构：一个卷积层 -> ReLU激活 -> 最大池化 -> 全连接层"""

    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc = nn.Linear(in_features=16 * 14 * 14, out_features=10)

    def forward(self, x):
        x = self.pool(self.relu(self.conv(x)))
        x = x.view(-1, 16 * 14 * 14)
        x = self.fc(x)
        return x


# ---------- 4.3 数据加载与预处理 ----------
def load_data(batch_size=64):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    train_dataset = torchvision.datasets.MNIST(
        root='./data', train=True, download=True, transform=transform
    )
    test_dataset = torchvision.datasets.MNIST(
        root='./data', train=False, download=True, transform=transform
    )
    train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True
    )
    test_loader = torch.utils.data.DataLoader(
        test_dataset, batch_size=batch_size, shuffle=False
    )
    return train_loader, test_loader


# ---------- 4.4 训练函数 ----------
def train(model, train_loader, criterion, optimizer, device, epochs=5):
    model.train()
    train_losses = []
    for epoch in range(epochs):
        running_loss = 0.0
        correct = 0
        total = 0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
        epoch_loss = running_loss / len(train_loader)
        epoch_acc = 100 * correct / total
        train_losses.append(epoch_loss)
        print(f'Epoch {epoch+1}/{epochs}, Loss: {epoch_loss:.4f}, Accuracy: {epoch_acc:.2f}%')
    return train_losses


# ---------- 4.5 测试函数 ----------
def test(model, test_loader, criterion, device):
    model.eval()
    test_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            test_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    test_loss /= len(test_loader)
    accuracy = 100 * correct / total
    print(f'Test Loss: {test_loss:.4f}, Accuracy: {accuracy:.2f}%')
    return test_loss, accuracy


# ---------- 4.6 可视化函数 ----------
def display_data(data_loader, num_images=25):
    dataiter = iter(data_loader)
    images, labels = next(dataiter)
    grid_size = int(np.ceil(np.sqrt(num_images)))
    plt.figure(figsize=(10, 10))
    for i in range(min(num_images, images.shape[0])):
        plt.subplot(grid_size, grid_size, i+1)
        img = images[i][0].cpu().numpy()
        plt.imshow(img, cmap='gray')
        plt.title(f'Label: {labels[i]}')
        plt.axis('off')
    plt.tight_layout()
    plt.savefig('mnist_samples.png')
    plt.show()


def visualize_predictions(model, test_loader, device, num_images=5):
    model.eval()
    dataiter = iter(test_loader)
    images, labels = next(dataiter)
    images, labels = images.to(device), labels.to(device)
    outputs = model(images)
    _, predicted = torch.max(outputs, 1)
    images = images.cpu()
    plt.figure(figsize=(12, 4))
    for i in range(min(num_images, images.shape[0])):
        plt.subplot(1, num_images, i+1)
        img = images[i][0].numpy()
        plt.imshow(img, cmap='gray')
        color = 'green' if predicted[i] == labels[i] else 'red'
        plt.title(f'Pred: {predicted[i]}\nTrue: {labels[i]}', color=color)
        plt.axis('off')
    plt.tight_layout()
    plt.savefig('predictions.png')
    plt.show()


# ---------- 4.7 主函数 ----------
def main():
    # 设置随机种子
    torch.manual_seed(42)

    # 选择设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device: {device}')

    # 加载数据
    train_loader, test_loader = load_data(batch_size=64)

    # 显示部分训练数据
    display_data(train_loader)

    # 创建模型
    model = SimpleCNN().to(device)
    print(model)

    # 定义损失函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # 训练模型
    train_losses = train(model, train_loader, criterion, optimizer, device, epochs=5)

    # 测试模型
    test_loss, test_accuracy = test(model, test_loader, criterion, device)

    # 可视化预测结果
    visualize_predictions(model, test_loader, device)

    # 保存模型
    torch.save(model.state_dict(), 'simple_cnn_mnist.pth')
    print('Model saved as simple_cnn_mnist.pth')

    # 绘制训练损失曲线
    plt.figure(figsize=(10, 5))
    plt.plot(train_losses, label='Training Loss')
    plt.title('Training Loss Over Epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.savefig('training_loss.png')
    plt.show()


# ---------- 4.8 程序入口 ----------
if __name__ == '__main__':
    main()