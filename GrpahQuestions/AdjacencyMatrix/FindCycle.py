class FindCycle:
    def findCycle(self, connections):
        cycles = 0
        for node, edges in connections.items():
            seen = set()
            if self.visitCheck(connections, node, seen, None):
                cycles += 1
        return cycles


    def visitCheck(self, connections, node, seen, parent):
        if node in seen:
            return True

        for edge in connections[node]:
            if edge == parent:
                continue
            seen.add(edge)
            if self.visitCheck(connections, edge, seen, node):
                return True
            seen.remove(edge)

        return False



object = FindCycle()
connections = {
    1: [2, 3, 4],
    3: [1, 4],
    4: [1, 3],
    2: [1, 6, 7],
    6: [2, 7],
    7: [2, 6]
}
print(object.findCycle(connections))