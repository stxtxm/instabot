import os
import logging
from dotenv import load_dotenv
import requests

load_dotenv()
logger = logging.getLogger(__name__)

API = "https://graph.facebook.com/v22.0/{}"

def post_to_facebook(image_path, caption):
    page_id = os.getenv("FACEBOOK_PAGE_ID")
    page_token = os.getenv("FACEBOOK_PAGE_TOKEN")

    if not page_id or not page_token:
        logger.error("FACEBOOK_PAGE_ID or FACEBOOK_PAGE_TOKEN not set")
        return False

    try:
        with open(image_path, "rb") as f:
            resp = requests.post(
                API.format(f"{page_id}/photos"),
                files={"source": f},
                data={"access_token": page_token, "published": "true"},
                timeout=60,
            )

        if resp.status_code != 200:
            logger.error(f"Photo upload failed: {resp.status_code} {resp.text}")
            return False

        photo_id = resp.json().get("id")
        logger.info(f"Photo uploaded: {photo_id}")

        resp = requests.post(
            API.format(f"{page_id}/feed"),
            data={
                "message": caption,
                "attached_media": f'[{{"media_fbid":"{photo_id}"}}]',
                "access_token": page_token,
            },
            timeout=60,
        )

        if resp.status_code == 200:
            post_id = resp.json().get("id")
            logger.info(f"Feed post created: {post_id}")
            return True

        logger.error(f"Feed post failed: {resp.status_code} {resp.text}")
        return False

    except FileNotFoundError:
        logger.error(f"Image not found: {image_path}")
        return False
    except Exception as e:
        logger.error(f"Post failed: {e}")
        return False