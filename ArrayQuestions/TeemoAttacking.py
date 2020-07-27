class Solution:
    def TeemoAttacking(self, timeSeries, duration):
        # if no attack took place, no fainting happened
        if not timeSeries:
            return 0

        # initialize result
        faint_duration = 0

        # apply first attack, wakeup time represent when will enemy wakeup
        wakeup_time = timeSeries[0] + duration
        prev_attack_time = timeSeries[0]

        # from second onward attacks
        for attack_time in timeSeries[1:]:

            # if teemo attacked before enemy woke up
            if attack_time < wakeup_time:
                # enemy's faint duration is increased by time elapsed between previous and current attacks
                faint_duration += (attack_time - prev_attack_time)

            # else teemo attacked after enemy woke up
            else:
                # enemy was fainted for entire duration
                faint_duration += duration

            # update wakeup time based on current attack
            wakeup_time = attack_time + duration
            prev_attack_time = attack_time

        # increase by duration for last attack
        faint_duration += duration

        # return total faint duration
        return faint_duration


object = Solution()
print(object.TeemoAttacking([1,4], 2))
print(object.TeemoAttacking([1,2], 2))