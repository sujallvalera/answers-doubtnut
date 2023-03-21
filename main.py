
import os
import time
import json
import requests
from bs4 import BeautifulSoup
from bs2json import BS2Json
from dotenv import load_dotenv

load_dotenv()

engine_id = os.getenv("engine_id")
api_key = os.getenv("api_key")
print(engine_id, api_key)
query = input("Enter the question to search upon:  ")
page = 1
start = (page - 1) * 10 + 1
url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={engine_id}&q={query}&start={start}"
data = requests.get(url).json()
search_items = data.get("items")
links = []
titles = []
for i, search_item in enumerate(search_items, start=1):
    try:
        long_description = search_item["pagemap"]["metatags"][0]["og:description"]
    except KeyError:
        long_description = "N/A"
    snippet = search_item.get("snippet")
    link = search_item.get("link")
    links.append(link)
    titles.append(snippet)

url1 = links[0]
r = requests.get(url1).text
soup = BeautifulSoup(r, "html.parser")
link = soup.find('script', {'id': '__NEXT_DATA__'})
# converts the bs4 object to a json
bs2json = BS2Json(link)
json_obj = bs2json.convert()
# mapping function to map to the source(mp4) file
script = json_obj['script']
text = script['text']
props = json.loads(text)
props1 = props['props']
pageProps = props1['pageProps']
videoData = pageProps['videoData']
vid_url = "https://videos.doubtnut.com/" + str(videoData['video_name'])
duration = int(videoData['duration']) / 60
title = videoData['title']
print(f"> {title}\n> Duration: {round(duration)}mins\n{vid_url}")

