from collections import defaultdict

class Solution:
    def subdomainVisitCount(self, cpdomains):
        hmap = defaultdict(int)
        for domain in cpdomains:
            items = domain.split()
            count = int(items[0])
            main_domain = items[1]

            subdomains = main_domain.split('.')
            for i in range(len(subdomains)):
                temp = '.'.join(subdomains[i:])
                hmap[temp] += count

        res = []
        for k, v in hmap.items():
            temp = ''.join(str(v) + " " + k)
            res.append(temp)

        return res


object = Solution()
print(object.subdomainVisitCount(["9001 discuss.leetcode.com"]))
print(object.subdomainVisitCount(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))