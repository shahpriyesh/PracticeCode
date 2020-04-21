from collections import Counter

class LongestStringChain:
    def longestStringChain(self, words):
        words.sort(key=len)
        smallest_word_len = len(words[0])
        longest_chain = 1

        for i in range(len(words)-1, 0, -1):
            word = words[i]
            chain = [word]
            last_attempt_len = len(word)

            for j in range(i-1, -1, -1):

                # if jth word's length is equal to current candidate than its definitely not a target to check
                if len(words[j]) == last_attempt_len:
                    continue

                # for a word to be predecessor of our current candidate, its length has be one lesser
                if len(words[j]) != last_attempt_len - 1:
                    break

                if len(self.findDiff(words[j], word)) == 1:
                    # current word is formed by jth word + any one additional char
                    # so now we want to treat ith word as current word
                    word = words[j]
                    chain.append(word)
                    last_attempt_len = len(word)

                    # OPTIMIZATION: if now, the word has only single character than we have found solution
                    if last_attempt_len == smallest_word_len:
                        break

            # update if this chain is longer than longest chain till now
            longest_chain = max(longest_chain, len(chain))

        return longest_chain

    def findDiff(self, s, t):
        return Counter(t) - Counter(s)


object = LongestStringChain()
print(object.longestStringChain(["a","b","ba","bca","bda","bdca"]))

# input is not in length sorted manner
print(object.longestStringChain(["sgtnz","sgtz","sgz","ikrcyoglz","ajelpkpx","ajelpkpxm","srqgtnz","srqgotnz","srgtnz","ijkrcyoglz"]))

# global longest chain needs to be found
print(object.longestStringChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]))

print(object.longestStringChain(["kfyptfirfpvca","iizclrlxc","mqmjram","ysxpfcgqdr","bhjx","osjifqfvsd","mgvkvmoghjna","xfffx","ilvrtkn","flt","eznrbhtpiuwozi","blfhzijxqgz","tzoyz","bottxkzs","hx","wsjkyzjulam","mfbqmjram","jilvrtkn","sjifqfvsd","zxeespjhxzisl","igfconeftek","ivrn","xpxbvuzgxatgi","mplfvwqydaf","oitanqdpurdr","hxfpfkfrx","sqd","sgik","mzjilpy","xujycmqhea","dlxrwaejznn","iiizclrlxac","ysxapfcgqdr","toz","f","xfff","mpfvwqd","mzjinlpy","oitanqdpurwzdr","mpclfvrwmqydaf","igfcetek","liriplczauq","xpxbvuzgati","tzfoyz","izlrlxc","xbvgi","xwsjkuyjpzjulam","lirqiplczoadscuq","wjgilvnrgtknpt","dlhxrwaejznn","dxwaejznn","sflt","gdibclem","zxekvespjhxzisl","ibgfconeftek","sjifqfsd","xpxbvuzgxati","irip","swygipgoukil","kfyptfirfnpvca","bfhzijxqgz","qjnjsxghflte","bhjxz","bktdibwrrbn","xjch","svrbrxkbfrjb","xpxbvgai","olgdjrusqjx","iizclrlxac","iripuq","xch","njsxhflte","fkfmk","ri","xujyacmqhehla","pxbvgi","mbqmjram","igfcnetek","oitanqdpurwdr","mqjam","xpxbvuzlgxatgi","fwd","kfyptfirfnpvcza","bfhijxqgz","mpfvwqdaf","ch","mswygipgzoukil","iiizclrlxfbadcb","swygigok","flkfmk","mpfvwqydaf","ysxpcgqdr","igfconetek","bxavkbailbad","oitanqdrpurwzdr","igfetek","mubbijvfrmy","pfwd","nrbhtpiuozi","dwejznn","mfbmqmjram","liriplczoacuq","rxlujyacmqhehla","zxevespjhxzisl","sfqfsd","wjilvnrtknpt","jilvrtknp","jsxflt","xujcmqh","kfogoicadrhlwzje","gfetek","h","iripczuq","gkvmoghjna","swygipgzoukil","kyptfrfpvca","btxzs","sqfd","xpxbvgi","ffk","ibgfconepftek","mpclfvwmqydaf","sygik","xpxbvuezlgxatgi","swygipgokl","xpxbvugati","bhjxqz","ofwhchg","xavkbailbad","f","iripcuq","sifqfsd","xujyacmqhea","ilvrtn","mpfwqd","xujycmqh","olgdjrusjx","qnjsxhflte","xfffrx","bcnkdtdibwrrhbn","xujcmh","bnktdibwrrhbn","hvxfpfkfrx","xpxbvueezlgxatgi","mpfwd","aflkfmk","fl","sfqfd","rn","tzoz","xpxbvugai","wsjkuyjzjulam","znrbhtpiuwozi","bnkdtdibwrrhbn","zxekvespyjhxzisl","kyptfirfpvca","ffmk","jcevcbtqkbmweoko","yptfrfpva","xujycmqhe","qnjsxghflte","mqjram","swygiok","iizlrlxc","mzgvkvmoghjna","jilvnrtknpt","wjgilvnrtknpt","onz","wsjkyjzjulam","ivrtn","liriplczoauq","zmfbmqmjram","bcnkdtdibwrrhbxn","i","jilvrtknpt","xffkfrx","rxujyacmqhehla","xujyacmqhela","bttxkzs","bktdibwrrhbn","wjz","xwsjkuyjzjulam","blfhpzijxqgz","araodwbanb","iripczauq","rbhtpiuoz","osjifrqfvsd","liripczauq","mgkvmoghjna","iri","iripu","scvrbrxkbfrjb","dxwejznn","hvxfpfkyfcprx","gdibcletm","jsflt","xvi","yspcgqdr","lirqiplczoascuq","gdibcletmj","bhx","njsxhflt","xvgi","on","bhijxqgz","liriplczoascuq","fff","swygipgoukl","oitanqdrpurwzrdr","hvxfpfkyfprx","iiizclrlxfbac","swygik","bhjxqgz","iiizclrlxbac","bttxzs","dlxwaejznn","dwejzn","xv","getek","hvxfpfkyfrx","znrbhtpiuozi","araohdwbanb","mplfvwmqydaf","zmfbmqmjrawm","iiizclrlxfbacb","ff","araohdwbanbq","xjcmh","wjzn","jsxhflt","hxffkfrx","ff","irn","wejzn","gdibclm","yptfrfpvca","mpfvwqda","swygipgok","mzvgvkvmoghjna","rbhtpiuozi"]))