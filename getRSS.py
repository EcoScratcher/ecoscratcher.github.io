import json
import os

import feedparser

feedURL = "https://explorethemetaverse.substack.com/feed"
fileLocation = "/home/runner/work/ecoscratcher.github.io/ecoscratcher.github.io/eotm-article-data.json"

feedData = feedparser.entries

with open(fileLocation, "w") as fp:
    json.dump(feedData, fp)
