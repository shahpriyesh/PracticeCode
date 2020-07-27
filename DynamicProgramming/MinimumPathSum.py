class Solution:
    def MinimumPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        dp = [[0 for i in range(n)] for j in range(m)]

        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]


object = Solution()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(object.MinimumPathSum(grid))










# We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

# Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

# Sample input:

# user0 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
# user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
# user2 = ["a", "/one", "/two"]
# user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
# user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
# user5 = ["a"]

# Sample output:

# findContiguousHistory(user0, user1)
#    /pink
#    /register
#    /orange

# findContiguousHistory(user1, user2)
#    (empty)

# findContiguousHistory(user2, user0)
#    a

# findContiguousHistory(user5, user2)
#    a

# findContiguousHistory(user3, user4)
#    /plum
#    /blue
#    /tan
#    /red

# findContiguousHistory(user4, user3)
#    /plum
#    /blue
#    /tan
#    /red

# n: length of the first user's browsing history
# m: length of the second user's browsing history


from collections import defaultdict
import pprint

user0 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue",
         "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender",
         "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]


def findContiguousHistory(user1, user2):  # O(n * m * min(m, n))
    if len(user1) == 0 or len(user2) == 0:
        return 0

    final_res = []
    for i in range(len(user1)):  # O(n)
        curr_res = []  # O(n)
        for j in range(len(user2)):  # O(m)
            if user1[i] == user2[j]:
                k, l = i, j

                while k < len(user1) and l < len(user2):  # O(min(m, n))
                    if user1[k] == user2[l]:
                        curr_res.append(user1[k])
                    else:
                        break
                    k += 1
                    l += 1

            if len(curr_res) > len(final_res):
                final_res = curr_res

    return final_res


print(findContiguousHistory(user0, user1))
print(findContiguousHistory(user1, user2))
print(findContiguousHistory(user2, user0))
print(findContiguousHistory(user5, user2))
print(findContiguousHistory(user3, user4))
print(findContiguousHistory(user4, user3))

# def calculateClicksByDomain(counts):
#     hmap = defaultdict(int) # O(n)

#     for count in counts:    # O(n)
#         items = count.split(',')
#         # item [count, domain]

#         count = int(items[0])
#         domain = items[1]
#         subdomains = domain.split('.')

#         for i in range(len(subdomains)):    # O(constant)
#             curr = '.'.join(subdomains[i:])
#             hmap[curr] += count

#     return hmap