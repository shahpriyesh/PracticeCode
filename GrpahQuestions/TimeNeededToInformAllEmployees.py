class TimeNeededToInformAllEmployees:
    def __init__(self):
        self.sub_map = {}

    def timeNeeded(self, n, headID, manager, informTime):
        self.sub_map = {}
        for i in range(len(manager)):
            if manager[i] in self.sub_map:
                self.sub_map[manager[i]].append(i)
            else:
                self.sub_map[manager[i]] = [i]
        return self.util(headID, manager, informTime)

    def findSubordinates(self, headID, manager):
        return self.sub_map[headID] if (headID in self.sub_map) else []

    def util(self, headID, manager, informTime):
        orig_time = informTime[headID]
        time = 0
        subs = self.findSubordinates(headID, manager)
        for sub in subs:
            time = max(time, orig_time + self.util(sub, manager, informTime))
        return time


object = TimeNeededToInformAllEmployees()
n = 1
headID = 0
manager = [-1]
informTime = [0]
print(object.timeNeeded(n, headID, manager, informTime))
n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
print(object.timeNeeded(n, headID, manager, informTime))
n = 7
headID = 6
manager = [1,2,3,4,5,6,-1]
informTime = [0,6,5,4,3,2,1]
print(object.timeNeeded(n, headID, manager, informTime))
n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
print(object.timeNeeded(n, headID, manager, informTime))
n = 4
headID = 2
manager = [3,3,-1,2]
informTime = [0,0,162,914]
print(object.timeNeeded(n, headID, manager, informTime))