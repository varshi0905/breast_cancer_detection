import torch
import torch.nn as nn
import torch.nn.functional as F
from app.config import MODEL_PATH, CLASSES
from app.utils import preprocess_image

device = torch.device("cpu")

class BasicBlock(nn.Module):
    expansion = 1
    
    def __init__(self, in_channels, out_channels, stride=1):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels,
                               kernel_size=3, stride=stride,
                               padding=1, bias=False)
        self.bn1   = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels,
                               kernel_size=3, stride=1,
                               padding=1, bias=False)
        self.bn2   = nn.BatchNorm2d(out_channels)
        
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels,
                          kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )
    
    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += self.shortcut(x)
        out = F.relu(out)
        return out


class ResNet18(nn.Module):
    def __init__(self, num_classes=1):
        super().__init__()
        self.conv1  = nn.Conv2d(3, 64, kernel_size=3,
                                stride=1, padding=1, bias=False)
        self.bn1    = nn.BatchNorm2d(64)
        self.layer1 = self.make_layer(64,  64,  block=2, stride=1)
        self.layer2 = self.make_layer(64,  128, block=2, stride=2)
        self.layer3 = self.make_layer(128, 256, block=2, stride=2)
        self.layer4 = self.make_layer(256, 512, block=2, stride=2)
        self.ada     = nn.AdaptiveAvgPool2d((1, 1))
        self.dropout = nn.Dropout(0.5)
        self.fc      = nn.Linear(512, num_classes)
    
    def make_layer(self, in_channels, out_channels, block, stride):
        layers = []
        layers.append(BasicBlock(in_channels, out_channels, stride))
        for _ in range(1, block):
            layers.append(BasicBlock(out_channels, out_channels, stride=1))
        return nn.Sequential(*layers)
    
    def forward(self, x):
        x = F.relu(self.bn1(self.conv1(x)))
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.ada(x)
        x = torch.flatten(x, 1)
        x = self.dropout(x)
        x = self.fc(x)
        return x


# Load model at startup
model = ResNet18(num_classes=1)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.eval()

def predict(image_bytes: bytes) -> dict:
    tensor = preprocess_image(image_bytes).to(device)
    with torch.no_grad():
        output = model(tensor)
        prob = torch.sigmoid(output).item()
    
    label = CLASSES[1] if prob >= 0.5 else CLASSES[0]
    confidence = round(prob * 100, 2) if prob >= 0.5 else round((1 - prob) * 100, 2)
    
    return {
        "label": label,
        "confidence": confidence
    }