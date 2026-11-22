# Pet Peeve Tees — daily social post playbook

Used by the daily scheduled task that makes one post per day for Instagram (@petpeevetees) and TikTok (@petpeevetees), saved to Buffer as drafts for Joe to approve.

## Brand
- Voice: dry, relatable, a little sarcastic. "T-shirts that share what you won't say out loud." Never mean-spirited, never political, no profanity.
- Colors: dark slate #2E3B3E, cream #F6EFE3, red #B3262E, yellow #F2C94C.
- Font: Poppins Bold / Medium (/usr/share/fonts/truetype/google-fonts/).
- Logo: "PET / PEEVE / TEES" stacked in a circle (see `logo()` in tools/sample_build.py).
- Every post points to the website: captions end with "petpeevetees.com (link in bio)". Never send people to Etsy or Amazon.
- Facts we can state: unisex sizes S–5XL, free US shipping on petpeevetees.com, the color count from library/designs.json. Don't feature a third-party logo (e.g. the Facebook logo on Stop Asking If It's Available) as the main visual of a post. Do not mention prices, discounts or codes unless Joe asks.

## Formats (rotate by weekday)
- Mon: "Pet peeve of the week" short video, 9:16 1080x1920, 12–15 s, MP4 H.264 (-preset veryfast), silent audio track. Hook text → reaction beat → design close-up → model shot → end card.
- Tue: carousel, 4:5 1080x1350, 4–5 slides (title slide, design close-up, model, couple/flat, end card).
- Wed: "Which bugs you more? A or B" image, 4:5, two designs side by side, "Comment A or B".
- Thu: short video zoom on one design, 9:16, ~10 s.
- Fri: weekend / gift idea image or carousel ("For the friend who…").
- Sat: quote-card style image (the pet peeve as a bold statement + small shirt).
- Sun: light post — design close-up with a relatable one-line caption.

## Source images
`library/<slug>/<color>_<view>.jpg` — views: design, flat-front, model-front, model-angle, model-back, couple. `library/designs.json` lists every design, its color count, which colors are in the library and which `views` exist. The first 17 designs have all six views; the other designs only have `design` and `flat-front` (no model photos) — for those, build posts from the close-up and flat shirt, and prefer the 17 full designs for video and couple/model-heavy formats. Never alter the shirt art itself.

## Rotation
`history.json` records what was posted. Don't feature the same design twice within 10 days; spread golf designs (Rake The Bunker, Put The Flag Back, Replace Your Divot) and work/home/road designs evenly. Spoiler Chicago is a niche inside-joke design — use rarely. Boston designs (Fix The T, Pave The Roads) fit local/Boston-themed days.

## Posting times (America/New_York) — based on 2026 Buffer, Sprout Social, Metricool and HubSpot studies
| Day | Instagram | TikTok |
|---|---|---|
| Mon | 12:15 PM | 7:30 PM |
| Tue | 12:15 PM | 7:30 PM |
| Wed | 12:15 PM | 7:30 PM |
| Thu | 12:15 PM | 7:30 PM |
| Fri | 11:45 AM | 7:30 PM |
| Sat | 11:15 AM | 10:45 AM |
| Sun | 7:45 PM | 9:15 AM |
Review after 3–4 weeks against Instagram Insights / TikTok Studio follower-activity data and adjust.

## Reach & tagging best practices
- Instagram allows at most 5 hashtags per post/Reel (hard limit since Dec 2025) — use exactly 5: #petpeevetees (branded) + #petpeeves + 1–2 topic tags for the design (e.g. #misophonia, #officehumor, #golfhumor, #dogmom, #roadrage) + 1 product/occasion tag (#funnytshirts, #giftsforhim, #giftsforher, #holidaygiftideas, #fathersdaygift…). No generic spam tags (#fyp, #instagood).
- TikTok: 3–5 hashtags, and put plain search keywords in the caption itself ("funny t-shirt", "gift idea", the pet peeve in words) — TikTok search reads captions.
- First line = hook (it's all people see before "more"). Ask for a comment ("Comment A or B", "Tag the person who…") — comments and shares drive distribution to non-followers.
- Instagram: images/carousels 4:5, video as Reels with shouldShareToFeed true. Carousels get re-shown to people who didn't swipe.
- Video: hook in the first second, on-screen text (most watch muted), under 15 s.
- Seasonal angles: Nov–Dec = gift framing (Black Friday 11/27, Cyber Monday 11/30, "order by Dec 15 for Christmas delivery" is on the site banner). Golf designs in spring/summer and Father's Day; back-to-school/office designs in Sept.
- Every post: one design focus, clear "petpeevetees.com (link in bio)" call to action.

## Publishing
1. The daily run makes TOMORROW's post (America/New_York date + 1). Render media, commit to `posts/YYYY-MM-DD/` (the post's date), push.
2. Public URL: https://raw.githubusercontent.com/PetPeeveTees/petpeevetees-media/main/posts/YYYY-MM-DD/<file>
3. Buffer: create_post with mode "customScheduled", dueAt = that day's time from the table above (ISO with the correct -05:00/-04:00 offset), schedulingType "automatic", one post per channel. Instagram: metadata.instagram {type: post|reel, shouldShareToFeed: true}. TikTok: metadata.tiktok {title}. Joe reviews the preview and can edit or delete in Buffer before it goes out.
4. Cleanup: delete `posts/` folders older than 7 days.
