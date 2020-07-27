class Solution:
    def twoCityScheduling(self, costs):
        N = len(costs)
        per_city = N // 2
        total = 0

        # construct an array of tuples of (candidate number, cost difference between two cities)
        relative_costs = [(i, item[0]-item[1]) for i, item in enumerate(costs)]

        # sort by cost difference so that all candidates that are cheaper to send to city A are in first N/2 spaces
        relative_costs.sort(key=lambda x: x[1])

        # for first N/2 candidates add city A cost
        for rc in relative_costs[:per_city]:
            candidate = rc[0]
            total += costs[candidate][0]

        # for next N/2 candidatese add city B cost
        for rc in relative_costs[per_city:]:
            candidate = rc[0]
            total += costs[candidate][1]

        return total


    def twoCityScheduling_INCORRECT(self, costs):
        N = len(costs)
        per_city_N = N // 2
        costs = [(i, x) for i, x in enumerate(costs)]

        # sort by cost of A and choose first N // 2 elements
        city_A = sorted(costs, key=lambda x: x[1][0])
        city_B = sorted(costs, key=lambda x: x[1][1])

        city_A_result = city_A[:per_city_N]
        city_B_result = city_B[:per_city_N]

        a_idx = per_city_N
        b_idx = per_city_N

        for item in costs:
            candidate = item[0]
            cityA_cost = item[1][0]
            cityB_cost = item[1][1]

            if item in city_A_result and item in city_B_result:
                if cityA_cost >= cityB_cost:
                    city_A_result.remove(item)
                    while city_A[a_idx] in city_B_result:
                        a_idx += 1
                    city_A_result.add(city_A[a_idx])
                else:
                    city_B_result.remove(item)
                    while city_B[b_idx] in city_A_result:
                        b_idx += 1
                    city_B_result.add(city_B[b_idx])

        total = 0
        for item in city_A_result:
            total += item[1][0]

        for item in city_B_result:
            total += item[1][1]

        return total


object = Solution()
print(object.twoCityScheduling([[10,20],[30,200],[400,50],[30,20]]))
print(object.twoCityScheduling([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))