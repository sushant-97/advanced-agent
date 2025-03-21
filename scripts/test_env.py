import os
import torch
import transformers

def test_environment():
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA device: {torch.cuda.get_device_name(0)}")
    print(f"Transformers version: {transformers.__version__}")

    # Test importing other libraries
    try:
        import datasets
        print(f"Datasets version: {datasets.__version__}")

        import accelerate
        print(f"Accelerate version: {accelerate.__version__}")

        import wandb
        print(f"Weights & Biases version: {wandb.__version__}")

        print("\nAll essential libraries imported successfully!")
    except ImportError as e:
        print(f"Error importing libraries: {e}")

if __name__ == "__main__":
    test_environment()