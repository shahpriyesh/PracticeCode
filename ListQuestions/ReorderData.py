class ReorderData:
    def __init__(self):
        return;

    def reorderData(self, logs):

        digit_dict = {}
        letter_dict = {}
        response = []

        for log in logs:
            words = log.split(' ', 1)
            if "0" <= words[1][0] <= "9":
                self.insertInDict(digit_dict, words[1], words[0])
            else:
                self.insertInDict(letter_dict, words[1], words[0])

        self.sortDict(letter_dict)
        self.sortDict(digit_dict)

        for key, val in sorted(letter_dict.items()):
            for entry in val:
                response.append(entry + " " + key)

        for key, val in digit_dict.items():
            for entry in val:
                response.append(entry + " " + key)

        return response

    def insertInDict(self, dict, key, val):
        if key in dict:
            dict[key].append(val)
        else:
            dict[key] = []
            dict[key].append(val)

    def sortDict(self, dict):
        for key, val in dict.items():
            val.sort()


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
object = ReorderData()
print(object.reorderData(logs))