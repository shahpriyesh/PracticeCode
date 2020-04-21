class NumberOfAtoms:
    response = {}
    element = ""
    count = ""

    def numberOfAtoms(self, str, multiplier):
        str = str + '-'
        idx = 0
        while idx < len(str):
            if 'A' <= str[idx] <= 'Z':
                self.element_check(self.element, self.count, multiplier)
                # start constructing new element
                self.element += str[idx]
            elif 'a' <= str[idx] <= 'z':
                # append character in current element
                self.element += str[idx]
            elif '0' <= str[idx] <= '9':
                self.count += str[idx]
            elif str[idx] == '-':
                self.element_check(self.element, self.count, multiplier)
            elif str[idx] == '(':
                # if any element is already found than insert in dictionary first
                self.element_check(self.element, self.count, multiplier)

                open_location, close_location = idx, 0
                open_cnt, close_cnt = 1, 0
                while open_cnt != close_cnt:
                    idx = idx + 1
                    if str[idx] == '(':
                        open_cnt += 1
                    elif str[idx] == ')':
                        close_cnt += 1
                close_location = idx
                temp = str[open_location+1: close_location]

                inner_multiplier = ""
                idx = idx + 1
                while '0' <= str[idx] <= '9':
                    inner_multiplier += str[idx]
                    idx = idx + 1

                if inner_multiplier == "":
                    self.numberOfAtoms(temp, 1*multiplier)
                else:
                    self.numberOfAtoms(temp, int(inner_multiplier)*multiplier)
                idx = idx - 1

            idx = idx + 1

        return self.response_printer()

    def insert(self, element, count):
        if element not in self.response:
            self.response[element] = count
        else:
            self.response[element] += count

    def element_check(self, element, count, multiplier):
        # if any element is already found than insert in dictionary first
        if element != "":
            if count == "":
                self.insert(element, 1*multiplier)
            else:
                self.insert(element, int(count)*multiplier)
        self.element = ""
        self.count = ""

    def response_printer(self):
        response_str = ""
        for key in sorted(self.response.keys()):
            if self.response[key] == 1:
                response_str = response_str + key
            else:
                response_str = response_str + key + str(self.response[key])
        return response_str


object = NumberOfAtoms()
print(object.numberOfAtoms("Mg(OH)2", 1))
