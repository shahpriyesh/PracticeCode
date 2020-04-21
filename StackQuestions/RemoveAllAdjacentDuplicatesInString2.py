class RemoveAllAdjacentDuplicatesInString2:
    def removeAllAdjacentDuplicates(self, s, k):
        i = 0
        while i+k-1 < len(s):
            # check if adjacent characters are matching
            match_cnt = 1
            for j in range(i+1, i+k):
                if s[i] != s[j]:
                    break
                match_cnt += 1

            if match_cnt == k:
                # remove adjacent characters (from i to i+k)
                s = s[:i] + s[i+k:]
                # try the previous character if it matches with the updated next one
                i = i - k if i - k > 0 else 0
            else:
                # just move to next character
                i = i + 1

        return s

    def removeAllAdjacentDuplicatesUsingStack(self, s, k):
        # create stack [character, count of occurence] (with a dummy entry to avoid empty stack situation)
        stack = [['#', 0]]
        for c in s:
            # check if character matches the character that is on top of stack
            if stack[-1][0] == c:
                # increment the count
                stack[-1][1] += 1
                # check if count has become equal to k, than we found that these characters adjacent occurences needs
                # to be removed
                if stack[-1][1] == k:
                    stack.pop()
            else:
                # if match is not found than simply push this new character with count 1
                stack.append([c, 1])

        # constrcut string from stack and return
        return ''.join(stack[i][0] * stack[i][1] for i in range(1, len(stack)))


object = RemoveAllAdjacentDuplicatesInString2()
print(object.removeAllAdjacentDuplicatesUsingStack("abcd", 2))
print(object.removeAllAdjacentDuplicatesUsingStack("deeedbbcccbdaa", 3))
print(object.removeAllAdjacentDuplicatesUsingStack("pbbcggttciiippooaais", 2))

# Index out of range
print(object.removeAllAdjacentDuplicatesUsingStack("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))

# Time Limit Exceeded
print(object.removeAllAdjacentDuplicatesUsingStack("xwjoxghzelkikczhsofyczfalazmrkyfwedmagzrgvuwoflccqwxotvmrdyeadhbqgkgywukxkhyzz"
                                         "qpszgvylcwlsbmqkjmymfxqmtuawjagdauiygrsfwpgbrdsxccwfyypdkdvrhwukkxxvqjgqoplznvifafdmvipdtdnmtdmokhaaeuflrkdbdoxse"
                                         "ljjudatscfopkasdahehkagratmewnitwuwbszfpmcwfghqpmgysznutnjspvnxxpmrgbvajnmrpoyzxmxpaxdogbibvaujrawioslaampjbdkntuoh"
                                         "ctfeyzdvpkhiwnirjcvkpovcdouxxwpeakqgmdvcvtggkpmthgoieibnjbqlihwjbchxkfarxbgcxgwlbvkwkezwwlmoxmcruttwwgnsihvffbsztpzlbhjcaqmblqoohkuudjnsuknmjpfwxwpcvegkmbpigwdshjtuwtr"
                                         "bcugcmnmmdnhltbufdrupvyliaaszgrjnkizqxyizqvrobetbadpmchggdvmuiqizawiiudfjdledgfyflzjilwlczhxejlbppcghgvldsqwyxttqpoundwossxrtlwcemnfdgopfaz"
                                         "ffuftpnnenofbielneghtygnlafdycqaeecpcezxboupfblpcqfmoyaulfugdxyqfrfqokchrxxheihptcmgetxtnnrivangmyvsuynoeougzpruttcrakrymfbjhylqyuyofzkpkfpvdzhjb"
                                         "pswylockgngzdcjaudymrqymoyaeljmxlqogfrsbriokdekiueczmuzeciygugigobxivmojrseaaxnkzohvxlirwyxloarjmkhzjlxmqpcdxnusazopfbtmuaqxtttenmomacr"
                                         "dqftqxsmwyixdpcqpaygxqlgelvjqsptmcpdlwcezwtprryblqtnwbstilgwgeyofsnaqkzqfaiotqvnsiotxfvpbuwzmopmnszepluomze", 10000))