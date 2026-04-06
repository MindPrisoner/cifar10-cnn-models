# CIFAR10 CNN 项目

这是一个围绕 CIFAR10 图像分类展开的 CNN 实验项目，覆盖了 LeNet、AlexNet 和 ResNet18 等模型结构，并记录了数据增强、BatchNorm、Dropout 以及学习率调度策略对训练效果的影响。

## 项目定位

- 在 CIFAR10 上比较不同 CNN 结构的表现
- 观察数据增强对泛化能力的影响
- 记录 BatchNorm、Dropout 和 Scheduler 的作用
- 对比不同学习率策略下的 accuracy 变化

## 目录结构

```text
cifar10_cnn/
├── configs/
│   └── config.py          # 训练超参数
├── datasets/
│   └── cifar10_dataset.py # CIFAR10 加载与增强
├── engine/
│   ├── trainer.py         # 训练逻辑
│   └── evaluator.py       # 评估逻辑
├── models/
│   ├── alexnet.py         # AlexNet 结构
│   └── resnet.py          # ResNet18 结构
├── utils/
│   ├── logger.py         # TensorBoard 日志
│   └── seed.py           # 随机种子固定
├── train.py              # 训练入口
├── test.py               # 测试脚本预留
├── requirements.txt      # 依赖列表
└── README.md
```

## 数据集

项目使用 `torchvision.datasets.CIFAR10`。

训练集包含随机裁剪和随机翻转等增强策略，测试集只保留基础归一化处理。

## 模型与实验

项目中保留了多个模型版本：

- `LeNet`
- `AlexNet`
- `ResNet18`

训练入口当前使用的是 `ResNet18`，并配合学习率调度器进行训练。

项目的实验重点包括：

- CIFAR10 数据增强
- BatchNorm
- Dropout
- StepLR / 其他调度策略
- Cosine LR
- Label Smoothing

## 训练流程

训练入口为：

```bash
python train.py
```

训练过程包括：

1. 固定随机种子
2. 加载 CIFAR10 数据集
3. 构建指定 CNN 模型
4. 使用交叉熵损失
5. 使用 Adam 优化器
6. 结合学习率调度器训练
7. 每个 epoch 后评估测试集 accuracy
8. 保存训练结果和模型权重

## 训练结果

该项目的核心输出是不同模型和不同策略下的 accuracy 对比。实际实验中可以清晰观察到：

- 更强的模型结构通常带来更高的分类准确率
- 数据增强对泛化能力有明显帮助
- 合理的学习率调度会让训练更稳定
- 在 CIFAR10 上，ResNet18 的整体表现通常优于更浅层的基础 CNN

## 备注

- `test.py` 当前为空，评估逻辑已放在 `engine/evaluator.py`
- 模型保存路径和训练参数统一配置在 `configs/config.py`
- 当前仓库重点是训练实验记录，不是推理服务项目

