import feedparser
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
FEEDS = [
    "https://vigiato.net/feed/",
    "https://digiato.com/feed/",
    "https://zoomg.ir/feed/"
]
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "disable_web_page_preview": False
    }
    requests.post(url, data=data)

def get_news():
    news_list = []

    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)
for item in feed.entries[:3]:
    title = item.title
    link = item.link

    image = None

    # گرفتن عکس از RSS (اگر وجود داشت)
    if "media_content" in item:
        image = item.media_content[0]["url"]
    elif "enclosures" in item and len(item.enclosures) > 0:
        image = item.enclosures[0].get("url")
            msg = f"""🎮 {title}

📺 تماشا 👈 {link}

HYDRA GX"""

            news_list.append(msg)

    return news_list


if __name__ == "__main__":
    for news in get_news():
      if image:
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
        data={
            "chat_id": CHANNEL_ID,
            "photo": image,
            "caption": msg
        }
    )
else:
    send_message(msg)
