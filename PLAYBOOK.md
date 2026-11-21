# Pet Peeve Tees — daily social post playbook

Used by the daily scheduled task that makes one post per day for Instagram (@petpeevetees) and TikTok (@petpeevetees), saved to Buffer as drafts for Joe to approve.

## Brand
- Voice: dry, relatable, a little sarcastic. "T-shirts that share what you won't say out loud." Never mean-spirited, never political, no profanity.
- Colors: dark slate #2E3B3E, cream #F6EFE3, red #B3262E, yellow #F2C94C.
- Font: Poppins Bold / Medium (/usr/share/fonts/truetype/google-fonts/).
- Logo: "PET / PEEVE / TEES" stacked in a circle (see `logo()` in tools/sample_build.py).
- Every post points to the website: captions end with "petpeevetees.com (link in bio)". Never send people to Etsy or Amazon.
- Facts we can state: unisex sizes S–5XL, free US shipping on petpeevetees.com, the color count from library/designs.json. Do not mention prices, discounts or codes unless Joe asks.

## Formats (rotate by weekday)
- Mon: "Pet peeve of the week" short video, 9:16 1080x1920, 12–15 s, MP4 H.264 (-preset veryfast), silent audio track. Hook text → reaction beat → design close-up → model shot → end card.
- Tue: carousel, 4:5 1080x1350, 4–5 slides (title slide, design close-up, model, couple/flat, end card).
- Wed: "Which bugs you more? A or B" image, 4:5, two designs side by side, "Comment A or B".
- Thu: short video zoom on one design, 9:16, ~10 s.
- Fri: weekend / gift idea image or carousel ("For the friend who…").
- Sat: quote-card style image (the pet peeve as a bold statement + small shirt).
- Sun: light post — design close-up with a relatable one-line caption.

## Source images
`library/<slug>/<color>_<view>.jpg` — views: design, flat-front, model-front, model-angle, model-back, couple. `library/designs.json` lists every design, its colors and color count. Never alter the shirt art itself.

## Rotation
`history.json` records what was posted. Don't feature the same design twice within 10 days; spread golf designs (Rake The Bunker, Put The Flag Back, Replace Your Divot) and work/home/road designs evenly. Spoiler Chicago is a niche inside-joke design — use rarely.

## Publishing
1. Render media, commit to `posts/YYYY-MM-DD/`, push.
2. Public URL: https://raw.githubusercontent.com/PetPeeveTees/petpeevetees-media/main/posts/YYYY-MM-DD/<file>
3. Buffer: create_post with saveToDraft=true, schedulingType=automatic, one draft per channel. Instagram: metadata.instagram {type: post|reel, shouldShareToFeed: true}. TikTok: metadata.tiktok {title}.
4. Cleanup: delete `posts/` folders whose Buffer posts have been sent (status sent), or that are older than 7 days.
