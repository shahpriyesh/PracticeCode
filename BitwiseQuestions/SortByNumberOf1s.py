class SortByNumberOf1s:
    def sortByNumberOf1s(self, arr):
        tmpList = [[] for i in range(32)]
        arr.sort()
        for num in arr:
            cnt = 0
            num_cpy = num
            while num_cpy:
                cnt += num_cpy & 1
                num_cpy >>= 1
            tmpList[cnt].append(num)

        res = []
        for tmp in tmpList:
            res.extend(tmp)

        return res


object = SortByNumberOf1s()
print(object.sortByNumberOf1s([0,1,2,3,4,5,6,7,8]))
print(object.sortByNumberOf1s([1024,512,256,128,64,32,16,8,4,2,1]))
print(object.sortByNumberOf1s([10000,10000]))
print(object.sortByNumberOf1s([2,3,5,7,11,13,17,19]))
print(object.sortByNumberOf1s([10,100,1000,10000]))