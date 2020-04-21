class GetWatchedVideosByYourFriedns:
    def getWatchedVideos(self, watchedVideos, friends, id, level):
        res = set()
        visited = set()
        self.findFriendsAtLevel(friends, id, level, visited, res)

        # Now we have list of friends at given level for given id
        # We will figure out videos watched by these friends
        suggestedVideos = {}
        for friend in res:
            videosSeen = watchedVideos[friend]
            for video in videosSeen:
                if video in suggestedVideos:
                    suggestedVideos[video] += 1
                else:
                    suggestedVideos[video] = 1

        # sort dictionary by value
        return [k for k, v in sorted(suggestedVideos.items(), key=lambda item: item[1])]

    def findFriendsAtLevel(self, friends, id, level, visited, res):
        if not level:
            if id not in visited:
                res.add(id)
            return

        visited.add(id)
        for friendID in friends[id]:
            self.findFriendsAtLevel(friends, friendID, level-1, visited, res)


object = GetWatchedVideosByYourFriedns()
watchedVideos = [["A", "B"], ["C"], ["B", "C"], ["D"]]
friends = [[1,2], [0,3], [0,3], [1,2]]
print(object.getWatchedVideos(watchedVideos, friends, 0, 1))
watchedVideos = [["A", "B"], ["C"], ["B", "C"], ["D"]]
friends = [[1,2], [0,3], [0,3], [1,2]]
print(object.getWatchedVideos(watchedVideos, friends, 0, 2))
watchedVideos = [["xk","qvgjjsp","sbphxzm"],["rwyvxl","ov"]]
friends = [[1],[0]]
# Expected= ["ov","rwyvxl"],  Output= ["rwyvxl","ov"]
print(object.getWatchedVideos(watchedVideos, friends, 0, 1))