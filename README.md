# Instabot

Generates unique AI images with French captions and posts them to a Facebook page every 2 hours.

## How it works

1. **Prompt** – AI generates a random creative image prompt via Pollinations text API
2. **Image** – generated from that prompt via Pollinations image API
3. **Caption** – AI writes a poetic French caption describing the image
4. **Post** – published to your Facebook page via Graph API

Every run produces unique content.

## Setup

Copy `.env.example` to `.env` and fill in your credentials:
```
FACEBOOK_PAGE_ID=your_page_id
FACEBOOK_PAGE_TOKEN=your_page_access_token
```
*(Token needs `pages_manage_posts` permission, valid ~60 days)*

## Run

```bash
docker compose up -d
```

## Cron

The container loops continuously: generates a post, then waits 1h-3h (random) before the next one.
