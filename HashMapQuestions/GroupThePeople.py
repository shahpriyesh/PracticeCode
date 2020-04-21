class GroupThePeople:
    def groupThePeople(self, groupSizes):
        groupMap = {}
        for i, gs in enumerate(groupSizes):
            if gs not in groupMap:
                groupMap[gs] = [[]]
            else:
                if len(groupMap[gs][-1]) == gs:
                    groupMap[gs].append([])
            groupMap[gs][-1].append(i)

        final = []
        for groupList in groupMap.values():
            final.extend(groupList)

        return final


object = GroupThePeople()
print(object.groupThePeople([3, 3, 3, 3, 3, 1, 3]))