#https://leetcode.com/problems/couples-holding-hands/

class CouplesHoldingHands:
    def __init__(self):
        pass

    # The following method simply puts correct person at correct place
    # every time it finds that a person is not at its place
    def nIntegerProblem_My(self, row):
        idx = 0
        swaps = 0
        while idx < len(row):
            if idx != row[idx]:
                row[row[idx]], row[idx] = row[idx], row[row[idx]]
                swaps = swaps + 1
            else:
                idx = idx + 1
        return row, swaps

    # The following method simply puts correct person at correct place
    # every time it finds that a person is not at its place
    def nIntegerProblem_Explained(self, row):
        idx = 0
        N = len(row)
        swaps = 0

        while idx < N:
            jdx = row[idx]
            while idx != jdx:
                row[idx], row[jdx] = row[jdx], row[idx]
                swaps += 1
                jdx = row[idx]
            idx += 1

        return row, swaps

    # The N couples problem can be solved using exactly the same idea as the N integers problem,
    # except now we have different placement requirements: instead of i == row[i],
    # we require i == ptn[pos[ptn[row[i]]]], where we have defined two additional arrays ptn and pos:
    #
    # ptn[i] denotes the partner of label i (i can be either a seat or a person)
    # - - ptn[i] = i + 1 if i is even; ptn[i] = i - 1 if i is odd.
    #
    # pos[i] denotes the index of the person with label i in the row array - - row[pos[i]] == i.
    #
    # The meaning of i == ptn[pos[ptn[row[i]]]] is as follows:
    #
    # The person sitting at seat i has a label row[i], and we want to place him/her next to his/her partner.
    #
    # So we first find the label of his/her partner, which is given by ptn[row[i]].
    #
    # We then find the seat of his/her partner, which is given by pos[ptn[row[i]]].
    #
    # Lastly we find the seat next to his/her partner's seat, which is given by ptn[pos[ptn[row[i]]]].
    def minSwapCouples(self, row):
        N = len(row)
        ptn = [0] * N
        curr_pos = [0] * N

        for i in range(N):
            val = i+1 if i % 2 == 0 else i-1
            ptn[i] = val
            curr_pos[row[i]] = i

        idx = 0
        swaps = 0
        while idx < N:
            # partner of the person who is sitting at current' person's partner's position.
            jdx = ptn[curr_pos[ptn[row[idx]]]]

            while idx != jdx:
                row[idx], row[jdx] = row[jdx], row[idx]
                curr_pos[row[idx]], curr_pos[row[jdx]] = curr_pos[row[jdx]], curr_pos[row[idx]]

                swaps += 1
                jdx = ptn[curr_pos[ptn[row[idx]]]]

            idx += 1

        return swaps



object = CouplesHoldingHands()
row = [0,4,2,1,5,3]
print(object.minSwapCouples(row))