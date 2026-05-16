import json
import logging
from perchance_scrapper import generate_image
from instagram_poster import post_to_instagram
import os

# Load Configuration
with open("config.json", "r") as f:
    config = json.load(f)

# Configure logging
LOG_LEVEL = config.get("log_level", "INFO").upper()
logging.basicConfig(level=getattr(logging, LOG_LEVEL), format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configuration
IMAGE_URL = config.get("generator_url")
SELECTOR = config.get("image_selector")
BUTTON_SELECTOR = config.get("button_selector")
WAIT_TIME = config.get("wait_time", 2000) # Default wait time of 2 seconds
IMAGE_PATH = "generated_image.png"
CAPTION = config.get("caption")

def main():
    logger.info(f"Generating image from {IMAGE_URL}...")
    # Add retry logic
    success = False
    for i in range(3):
        if generate_image(IMAGE_URL, IMAGE_PATH, selector=SELECTOR, button_selector=BUTTON_SELECTOR, wait_time=WAIT_TIME):
            success = True
            break
        logger.warning(f"Retrying generation... ({i+1}/3)")

    if not success:
        logger.error("Failed to generate image after retries. Exiting.")
        return
        return

    # logger.info("Posting to Instagram...")
    # if not post_to_instagram(IMAGE_PATH, CAPTION):
    #     logger.error("Failed to post to Instagram.")
    #     # We don't remove the image here, maybe we want to keep it
    #     return
    
    # Clean up
    if os.path.exists(IMAGE_PATH):
        os.remove(IMAGE_PATH)
    logger.info("Done.")

if __name__ == "__main__":
    main()
