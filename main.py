import feedparser
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

FEEDS = [
    "https://www.ign.com/rss/articles",
    "https://www.gamespot.com/feeds/mashup/"
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

            msg = f"""🎮 {title}

📺 تماشا 👈 {link}

HYDRA GX"""

            news_list.append(msg)

    return news_list


if __name__ == "__main__":
    for news in get_news():
        send_message(news)
