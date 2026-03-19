class Config:
    seed = 42

    #batch_size = 64
    batch_size = 128
    #epochs = 10
    # epochs = 20
    epochs = 50
    lr = 0.001
    #lr = 0.1
    num_workers = 4

    device = "cuda"

    #model_save_path = "checkpoints/mnist_model.pt"

    log_dir = "runs/cifar10"
    # model_save_path = "checkpoints/mnist_cnn.pth"
    #model_save_path = "checkpoints/mnist_cnn_LeNet.pth"
    # model_save_path = "checkpoints/cifar10_cnn_AlexNet.pth"
    model_save_path = "checkpoints/cifar10_resnet18.pth"