from collections import Counter

class DegreeOfArray:
    def __init__(self):
        pass

    def degreeOfArray(self, A):
        A_len = len(A)
        A_counter = Counter(A)
        num_list = A_counter.most_common()

        degree = num_list[0][1]
        most_repeated_nums = [num_list[0][0]]

        for idx in range(1, len(num_list)):
            if num_list[idx][1] == degree:
                most_repeated_nums.append(num_list[idx][0])

        answer = ""
        for num in most_repeated_nums:
            first_occurence = A.index(num)
            last_occurence = A_len - 1 - A[::-1].index(num)
            if answer == "" or answer > last_occurence - first_occurence + 1:
                answer = last_occurence - first_occurence + 1

        return answer


object = DegreeOfArray()
A = [3,4,3,3,4,3, 2,4,4]
print (object.degreeOfArray(A))