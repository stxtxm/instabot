from playwright.sync_api import sync_playwright
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_image(url, output_path, selector="img", button_selector=None, wait_time=2000):
    """
    Generates an image from a perchance generator.
    Optional: clicks a button_selector before taking a screenshot.
    """
    try:
        with sync_playwright() as p:
            logger.info("Launching browser...")
            browser = p.chromium.launch(headless=True)
            logger.info("Browser launched.")
            page = browser.new_page()
            logger.info(f"Navigating to {url}...")
            page.goto(url)
            logger.info("Navigation complete.")

            if button_selector:
                logger.info(f"Clicking button: {button_selector}")
                page.click(button_selector)
                # Wait for the network to be idle to ensure generation is likely complete
                page.wait_for_load_state('networkidle')
                page.wait_for_timeout(wait_time)

            # Wait for the element to be present
            logger.info(f"Waiting for selector: {selector}")
            page.wait_for_selector(selector)

            # Take a screenshot of the target element
            element = page.locator(selector).first
            logger.info("Taking screenshot...")
            element.screenshot(path=output_path)

            browser.close()
            logger.info(f"Image saved to {output_path}")
            return True
    except Exception as e:
        logger.error(f"An error occurred while scraping: {e}")
        return False
        return False

if __name__ == "__main__":
    # Placeholder URL - User needs to update this
    url = "https://perchance.org/ai-text-to-image-generator" 
    generate_image(url, "output.png")
