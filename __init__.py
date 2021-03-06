from mycroft import MycroftSkill, intent_file_handler

import os
import json
import requests
import xml.etree.ElementTree as ET

class SkillRecappNews(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.FEEDS = self.get_feeds()

    def get_feeds(self):
        skill_location = os.path.dirname(__file__)
        #rss_feeds.json in format: "name of feed, all matching descriptions" : "actual_url"
        with open(file=skill_location + "/rss_feeds.json", mode='r') as file:
            return json.load(file)


    @intent_file_handler('news.start.intent')
    def handle_news_recapp_skill(self, message):
        self.feed_url = self.select_feed(message)
        self.feed_structure = self.read_xml_to_dict(self.feed_url)
        self.articles = self.extract_articles(self.feed_structure)
        self.titles = self.extract_titles(self.articles)
        self.speak_dialog('news.start')

        counter = 0
        for title in self.titles:
            self.speak(title)
            counter += 1
            if (counter >= 5): # only read first 5 titles
                break

    def select_feed(self, message):
        # TODO
        return self.FEEDS.get("default news")

    def read_xml_to_dict(self, feed_url):
        response = requests.get(feed_url)
        return ET.fromstring(response.content)

    def extract_articles(self, feed_structure):
        return [item for item in feed_structure.iter('item')]

    def extract_titles(self, articles):
        return [title.find("title").text for title in articles]

def create_skill():
    return SkillRecappNews()

