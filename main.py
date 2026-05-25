import logging
import os
from generator import generate_prompt, generate_image, generate_caption
from publisher import post_to_facebook

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

IMAGE = "generated_image.png"

def main():
    prompt = generate_prompt()

    for i in range(3):
        if generate_image(prompt, IMAGE):
            break
        logger.warning(f"Retry {i+1}/3")
    else:
        logger.error("Failed to generate image")
        return

    caption = generate_caption(prompt)

    if post_to_facebook(IMAGE, caption):
        if os.path.exists(IMAGE):
            os.remove(IMAGE)
        logger.info("Done")
    else:
        logger.error("Failed to post")

if __name__ == "__main__":
    main()