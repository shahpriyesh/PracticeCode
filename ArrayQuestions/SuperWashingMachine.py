class SuperWashingMachine:
    def superWashingMachine(self, machines):
        res = 0
        avg = sum(machines) // len(machines)
        dress = sum(machines) % len(machines)
        if dress != 0:
            return -1
        machines.sort()
        idx_list = [i for i, val in enumerate(machines) if val <= avg]

        for idx in idx_list:
            res += avg - machines[idx]

        return res


object = SuperWashingMachine()
machines = [1, 0, 5]
print(object.superWashingMachine(machines))
machines = [0, 3, 0]
print(object.superWashingMachine(machines))
machines = [0, 2, 0]
print(object.superWashingMachine(machines))
machines = [4, 0, 0, 4]
print(object.superWashingMachine(machines))