class BestTimeToBuyAndSellStocks:
    def bestTimeToBuyAndSell(self, prices):
        if len(prices) < 2:
            return 0
        # Special case: if prices go only higher and higher
        for i, p in enumerate(zip(prices, sorted(prices))):
            if p[0] != p[1]:
                break
        if i == len(prices)-1:
            return prices[-1] - prices[0]

        final = 0
        for i in range(len(prices)-1):
            final = max(final, self.bt(prices, i, 0, 0))
        return final

    def bt(self, prices, start, curr, cnt):
        maxi = 0
        if cnt == 2:
            return curr
        if start >= len(prices):
            return curr if curr else 0
        buy = prices[start]
        for i in range(start+1, len(prices)):
            if prices[i] > buy:
                curr += (prices[i] - buy)
                maxi = max(self.bt(prices, i + 1, curr, cnt + 1), maxi)
                curr -= (prices[i] - buy)
        return maxi if maxi else curr


object = BestTimeToBuyAndSellStocks()
# print(object.bestTimeToBuyAndSell([3,3,5,0,0,3,1,4]))
# print(object.bestTimeToBuyAndSell([1,2,3,4,5]))
# print(object.bestTimeToBuyAndSell([7,6,4,3,1]))
# print(object.bestTimeToBuyAndSell([]))
# print(object.bestTimeToBuyAndSell([1]))
# print(object.bestTimeToBuyAndSell([2, 1]))
# print(object.bestTimeToBuyAndSell([1, 4, 2]))
# print(object.bestTimeToBuyAndSell([2, 1, 4]))
print(object.bestTimeToBuyAndSell([3,2,6,5,0,3]))