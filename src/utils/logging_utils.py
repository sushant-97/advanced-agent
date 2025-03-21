import logging
import os
import sys
from datetime import datetime

def setup_logging(log_level="INFO", log_file=None):
    """Set up logging configuration."""
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    # Create logs directory if it doesn't exist
    if log_file and not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))

    # Configure logging
    handlers = [logging.StreamHandler(sys.stdout)]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=handlers
    )

    return logging.getLogger()

def get_timestamp():
    """Get current timestamp string for filenames."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")