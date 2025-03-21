# Base configuration settings

# Model settings
MODEL_CONFIG = {
    "base_model_name": "mistralai/Mistral-7B-Instruct-v0.2",  # or another appropriate base model
    "tokenizer_name": "mistralai/Mistral-7B-Instruct-v0.2",
    "max_length": 2048,
    "use_4bit": True,  # For quantization
    "device": "cuda" if __import__("torch").cuda.is_available() else "cpu",
}

# Training settings
TRAINING_CONFIG = {
    "batch_size": 4,
    "gradient_accumulation_steps": 8,
    "learning_rate": 2e-5,
    "weight_decay": 0.01,
    "num_epochs": 3,
    "warmup_steps": 100,
    "logging_steps": 10,
    "evaluation_steps": 500,
    "save_steps": 1000,
}

# Data settings
DATA_CONFIG = {
    "train_file": "data/processed/train.json",
    "validation_file": "data/processed/validation.json",
    "test_file": "data/processed/test.json",
}

# Logging settings
LOGGING_CONFIG = {
    "wandb_project": "llm-alignment-project",
    "wandb_entity": None,  # Your wandb username or team
    "log_level": "INFO",
}