class BulbSwitcher3:
    def bulbSwitcher3(self, light):
        # set all bulb colors to OFF
        bulbsColor = [0]*(len(light)+1)
        # Just set 0th bulb as its just placeholder to BLUE
        bulbsColor[0] = 2

        allBlue = 0
        rightMost = 0

        for i in range(len(light)):
            # determine right most bulb that we turned on so far
            rightMost = max(rightMost, light[i])

            # Turn on bulb to yellow
            bulbLocation = light[i]
            bulbsColor[bulbLocation] = 1

            # if bulb to left of current location is already blue than this bulb will also turn blue
            if bulbsColor[bulbLocation - 1] == 2:
                bulbsColor[bulbLocation] = 2

                j = 0
                # turn all immediate next bulbs to blue
                for j in range(bulbLocation + 1, len(bulbsColor)):
                    if bulbsColor[j] == 1:
                        bulbsColor[j] = 2
                    else:
                        break

                # if any bulb to right of current location is yellow than this is not all blue status
                if bulbsColor[rightMost] != 1:
                    allBlue += 1

        return allBlue


object = BulbSwitcher3()
print(object.bulbSwitcher3([2,1,3,5,4]))
print(object.bulbSwitcher3([3,2,4,1,5]))
print(object.bulbSwitcher3([4,1,2,3]))
print(object.bulbSwitcher3([2,1,4,3,6,5]))
print(object.bulbSwitcher3([1,2,3,4,5,6]))
print(object.bulbSwitcher3([1]))