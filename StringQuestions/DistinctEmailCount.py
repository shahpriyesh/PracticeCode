class DistinctEmailCount:
    def __init__(self):
        pass

    def DistinctEmailCount(self, email_list):
        response = 0
        email_map = {}
        for email in email_list:
            data = email.split('@')
            truncated_email = data[0].split('+')
            final = truncated_email[0].replace('.','')

            if final in email_map:
                if data[1] not in email_map[final]:
                    email_map[final].append(data[1])
            else:
                email_map[final] = [data[1]]

        for email, domain_list in email_map.items():
            response += len(domain_list)

        return response

    def DistinctEmailCountBetterImpl(self, email_list):
        result = set()
        for email in emails:
            local, domain = email.split('@')
            if "+" in local:
                local = local[:local.index("+")]
            local = local.replace(".", "")
            result.add(local + "@" + domain)
        return len(result)


object = DistinctEmailCount()
email_list = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(object.DistinctEmailCount(email_list))