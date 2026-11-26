# Daily procedure for the "oranj joos" auto-poster (v2: no repo write access)

Channels: YouTube "oranj joos", Instagram @oranj_joos, TikTok @oranj_joos_animates. Posting goes through the Buffer connector (mcp__Buffer__*). Analytics + YouTube comments come from the Windsor connector (youtube).
The cloud session can READ the public repo https://github.com/microsoftbot6809-ai/gary-shorts but cannot write to it. The user drags new files to the repo by hand. Videos live at the repo root as `YYYY-MM-DD_<id>.mp4`; public URL = https://raw.githubusercontent.com/microsoftbot6809-ai/gary-shorts/main/<file>. Engine + docs live in `engine/`.
There is no state file you can write. State = (a) the repo's file list, (b) what Buffer already has scheduled/sent, (c) YouTube stats. Derive everything from those each run.

## Metadata
- Old videos (d01-d30, e01-e30): title + description in engine/manifest.json (by file name).
- New videos made by this automation: file `YYYY-MM-DD_v<MMDD>.mp4` where MMDD = the day you made it (so ids never clash), plus a sidecar text file with the same base name + `.txt`: line 1 = title (with 1-2 emoji), the rest = description. The user drags both into the repo root. Read sidecars from the repo for the top-up.

## 1. Top up Buffer (do this first; never skip)
- get_account (org id, timezone), list_channels (instagram, tiktok, youtube), list_posts for each channel with status scheduled and sent.
- Plan limit: 10 scheduled posts per channel. Free slots = 10 - scheduled count. Do not touch posts the user created by hand.
- Candidate videos = video files in the repo not yet used on that channel (match the file name inside each existing post's asset URL, scheduled OR sent). Order: new `v*` videos first (oldest first), then the old backlog in manifest order. Skip `*_d01.mp4`.
- Post time for each new post = the day after that channel's latest scheduled post, at 9:00 AM Pacific (zoneinfo America/Los_Angeles for the UTC offset), never in the past. One post per channel per day.
- create_post shape: mode customScheduled, schedulingType automatic, dueAt, text = title + "\n\n" + description, assets=[{"video":{"url": RAW_URL}}], plus metadata:
  * Instagram {"instagram":{"type":"reel","shouldShareToFeed":true}}
  * TikTok {"tiktok":{"title": <title, <= ~90 chars>}}
  * YouTube {"youtube":{"type":"short","title": <title>,"categoryId":"22","madeForKids":false,"privacy":"public"}} (check the tool schema)
- Verify the raw URL is reachable (HTTP 200) before posting. Never create duplicates.

## 2. Learn what people like (short, 3 steps)
- Windsor youtube get_data (call get_fields first): per video for Shorts published since 2026-11-25: video, video_title, views, engaged_views, average_view_percentage, likes, shares, comments (lifetime: video_view_count, video_like_count, video_comment_count). Ignore the channel's older non-cartoon videos.
- Buffer: get_aggregated_post_metrics / list_posts with includeMetrics for the last 31 days (Instagram + TikTok performance). Note the best and worst.
- YouTube comments (Windsor comment_* fields, last 14 days): note requests, favorite characters, "part 2" demands, jokes people quote.
Then decide today's video: copy what works (the characters, formats, hook style, length, topics of the top performers; continue a series people ask for), drop what flopped. Keep ~1 in 3 videos a deliberate new experiment. Quick WebSearch (2-3 queries) for what is trending in family-friendly animated comedy Shorts and seasonal moments in the next 2-4 weeks.

## 3. Make ONE new video
`bash engine/setup.sh` (once per session; downloads models), then read ENGINE.md and copy the structure of engine/stories_k.py into `engine/stories_v<MMDD>.py`. Write the story (25-48 s, hook in 2 s, one escalating joke, punchline ending, family friendly, no real people/brands/copyrighted characters; reuse the recurring cast). Then:
`python3 lint.py stories_v<MMDD>` (must print BAD 0) -> `python3 build.py stories_v<MMDD> render v<MMDD>` -> `python3 qa.py v<MMDD>` and LOOK at `out/qa_v<MMDD>.png` (Read it); fix problems and re-render. Duration must be < 60 s and mean volume about -16 dB.
Name outputs `YYYY-MM-DD_v<MMDD>.mp4` (YYYY-MM-DD = the nominal date, use the creation date) + the sidecar `.txt` (title; description ending "New animated Short every day. Subscribe for more!" then "#Shorts #Animation #Funny #Cartoon #Comedy"; series parts end with "Subscribe so you do not miss the next part!").

## 4. Deliver + notify
- SendUserFile the .mp4 and the .txt (status proactive).
- Finish with a SHORT plain message (this becomes the push notification). Start with "DRAG:" and the two file names, then one line: how many days of videos Buffer holds / are in the repo, and what you based the video on ("Gary part 1 did best, so ..."). If the repo has < 10 days of unqueued videos left, say it is urgent; otherwise "no rush".
- Mention problems (Buffer errors, missing engine folder, stale token) in one line.

## Don'ts
No credentials anywhere. No purchases/upgrades. Don't edit or delete the user's own posts. Don't change account settings.
