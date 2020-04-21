from collections import defaultdict
class CourseSchedule2:
    def courseSchedule2(self, numCourses, prerequisites):
        # map course -> list of prerequisites
        hmap = defaultdict(list)
        for prereq in prerequisites:
            hmap[prereq[0]].append(prereq[1])

        # keep a list of taken classes
        taken = []

        for course, prereqList in hmap.items():
            pass