from mycroft import MycroftSkill, intent_file_handler


class CourseworkSelection(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('selection.coursework1.intent')
    def handle_selection_coursework1(self, message):
        self.speak_dialog('selection.coursework1')

    @intent_file_handler('selection.coursework2.intent')
    def handle_selection_coursework2(self, message):
        self.speak_dialog('selection.coursework2')

    @intent_file_handler('selection.coursework3.intent')
    def handle_selection_coursework3(self, message):
        self.speak_dialog('selection.coursework3')

    @intent_file_handler('selection.coursework4.intent')
    def handle_selection_coursework4(self, message):
        self.speak_dialog('selection.coursework4')

    @intent_file_handler('selection.coursework5.intent')
    def handle_selection_coursework5(self, message):
        self.speak_dialog('selection.coursework5')



def create_skill():
    return CourseworkSelection()

