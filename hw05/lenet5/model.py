import torch
import torch.nn as nn
import torch.nn.functional as F

class LeNet5(nn.Module):
    def __init__(self):
        super(LeNet5, self).__init__()
        # 输入 1x28x28
        self.conv1 = nn.Conv2d(1, 6, 5)      # 28-5+1=24
        self.pool1 = nn.MaxPool2d(2, 2)      # 24/2=12
        self.conv2 = nn.Conv2d(6, 16, 5)     # 12-5+1=8
        self.pool2 = nn.MaxPool2d(2, 2)      # 8/2=4

        self.fc1 = nn.Linear(16*4*4, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool1(F.relu(self.conv1(x)))
        x = self.pool2(F.relu(self.conv2(x)))
        x = x.view(-1, 16*4*4)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x