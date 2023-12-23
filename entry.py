
class Entry:

    question = None
    answer = None
    url = None

    def __init__(self, question, answer, url):
        self.question = question
        self.answer = answer
        self.url = url

    def __eq__(self, other):
        if isinstance(other, Entry):
            if hash(self.question) == hash(other.question):
                return True
            else:
                return False
        return False

    def __hash__(self):
        return hash(self.question)
