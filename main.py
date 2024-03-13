from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent, LikeEvent, ShareEvent, FollowEvent, CommentEvent
import keyboard
import time
import asyncio

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="USER_ID", enable_detailed_gifts=True
)

@client.on("like")
async def on_like(event: LikeEvent):
    print(f"{event.user.unique_id} triggered forward.")
    keyboard.press('up')
    time.sleep(2)
    keyboard.release('up')

@client.on("gift")
async def on_gift(event: GiftEvent):
    if event.gift.id == 5655: #rose
        print(f"{event.user.unique_id} triggered right.")
        keyboard.press('right')
        keyboard.press('up')
        time.sleep(2)
        keyboard.release('up')
        keyboard.release('right')
    elif event.gift.id == 5269: #tiktok
        print(f"{event.user.unique_id} triggered left.")
        keyboard.press('left')
        keyboard.press('up')
        time.sleep(2)
        keyboard.release('up')
        keyboard.release('left')
    elif event.gift.id == 6104: #cap
        print(f"{event.user.unique_id} triggered reset.")
        keyboard.send('r')
    elif event.gift.id == 5487: #finger heart
        print(f"{event.user.unique_id} triggered reverse.")
        keyboard.press('down')
        time.sleep(2)
        keyboard.release('down')
    else:
        print(f"{event.user.unique_id} sent a different gift.")

@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"{event.user.unique_id} followed.")


async def run():
    while True:
        try:
            await asyncio.wait_for(client._start(), timeout=10)
        except TimeoutError:
            await asyncio.wait_for(client._start(), timeout=10)
            continue

asyncio.run(run())
