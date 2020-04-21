class ExclusiveTimeOfFunctions:
    def exclusiveTimeOfFunctions(self, n, logs):
        # list to hold final result, index=function_id, value=absolute time taken by function
        time_list = [0]*n

        # stack to hold function calls, each entry represents a node
        stack = []

        # go through each log
        for log in logs:
            # node contains [function_id, start_time, time_taken_by_functions_called_from_this_function]
            node = []

            # log will contain [function_id, "start" or "end", timestamp]
            log = log.split(':')
            log[0] = int(log[0])
            log[2] = int(log[2])

            if log[1] == "start":
                # create node from log and push in stack
                node.append(log[0])
                node.append(log[2])
                node.append(0)
                stack.append(node)
            else:
                if stack:
                    # take out last function entry
                    node = stack.pop()
                    # time taken = endTime - startTime + 1 - (any time taken by functions called from this function)
                    time_taken = log[2] - node[1] + 1 - node[2]
                    time_list[node[0]] += time_taken

                    if stack:
                        # take out previous function entry
                        node = stack.pop()
                        # update time taken by current function into the caller functions node entry
                        node[2] += time_taken
                        stack.append(node)

        return time_list


object = ExclusiveTimeOfFunctions()
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print(object.exclusiveTimeOfFunctions(n, logs))

n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(object.exclusiveTimeOfFunctions(n, logs))

n = 1
logs = ["0:start:0","0:start:1","0:start:2","0:end:3","0:end:4","0:end:5"]
print(object.exclusiveTimeOfFunctions(n, logs))