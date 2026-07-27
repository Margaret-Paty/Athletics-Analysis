import logging
from pathlib import Path


def setup_logger(name):
    log_folder = Path("logs")
    log_folder.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(
        log_folder / "pipeline.log"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger