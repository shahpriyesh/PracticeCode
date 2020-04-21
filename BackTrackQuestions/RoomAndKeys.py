class RoomAndKeys:

    def canVisitAllRooms(self, rooms):
        # hold a list of visited rooms till now
        visited = []

        # Go to visit room number 0
        visited = self.roomVisit(rooms, 0, visited)

        # if all the rooms that we could visit is equal to all the rooms that are present
        if len(visited) == len(rooms):
            return True

        # we couldn't visit all the rooms
        return False

    def roomVisit(self, rooms, key, visited):
        # append visited room in list
        visited.append(key)

        # go through keys that we received in this room
        for key in rooms[key]:
            # visit room with the available key if room hasn't already been visited
            if key not in visited:
                visited = self.roomVisit(rooms, key, visited)

        # return all visited rooms till now
        return visited

object = RoomAndKeys()
rooms = [[1,3],[3,0,1],[2],[0]]
print(object.canVisitAllRooms(rooms))