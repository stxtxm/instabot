# Perchance Instagram Bot

This project automates the process of scraping images from a [Perchance](https://perchance.org) generator and posting them to Instagram.

## Prerequisites

- Python 3.x
- `playwright` (with browser drivers)
- `instagrapi`

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```
2. Create a `.env` file with your Instagram credentials:
   ```env
   INSTA_USERNAME=your_username
   INSTA_PASSWORD=your_password
   ```
3. Configure the generator settings in `config.json`:
   ```json
   {
     "generator_url": "https://perchance.org/ai-text-to-image-generator",
     "image_selector": "img",
     "button_selector": "#randomize-button",
     "caption": "Check out this AI-generated image!"
   }
   ```

## Usage

Run the bot:
```bash
python main.py
```
