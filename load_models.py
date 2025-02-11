import logging
import os
from huggingface_hub import snapshot_download

# Configure logging
logging.basicConfig(level=logging.INFO)

def download_model():
    """
    Downloads the Manga OCR model from the Hugging Face Hub if it doesn't already exist locally.
    """
    model_dir = "models/manga-ocr"
    # Check if the folder exists and contains files
    if not os.path.exists(model_dir) or not os.listdir(model_dir):
        logging.info("Downloading Manga OCR model...")
        snapshot_download(repo_id="kha-white/manga-ocr-base", local_dir=model_dir)
        logging.info("Model downloaded successfully")
    else:
        logging.info("Model already exists and is not empty. Skipping download.")


if __name__ == "__main__":
    download_model()