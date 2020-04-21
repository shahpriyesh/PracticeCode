from collections import defaultdict

class GroupShiftedStrings:
    def groupShifted(self, strs):
        hmap = defaultdict(list)
        for strng in strs:
            diff_str = ""
            for i in range(1, len(strng)):
                diff_str = diff_str.join(str(ord(strng[i]) - ord(strng[i-1])))
            hmap[diff_str].append(strng)
        return hmap.values()


object = GroupShiftedStrings()
print(object.groupShifted(["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]))