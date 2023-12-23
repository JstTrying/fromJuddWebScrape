import csv


class CSVManager:

    __filename = ""
    __entries = set()

    def __init__(self, filename, entries):
        self.__filename = filename + ".csv"
        self.__entries = entries

    def save(self):
        header = ['question', 'answer', 'url']
        with open(file=self.__filename, mode='w', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for entry in self.__entries:
                list = [entry.question, entry.answer, entry.url]
                writer.writerow(list)

