from mycroft import MycroftSkill, intent_file_handler


class SkillRecappNews(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('news.recapp.skill.intent')
    def handle_news_recapp_skill(self, message):
        self.speak_dialog('news.recapp.skill')


def create_skill():
    return SkillRecappNews()

