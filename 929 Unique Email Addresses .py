"""929. Unique Email Addresses https://leetcode.com/problems/unique-email-addresses/ """

import time
from typing import List

class Solution:
    def numUniqueEmails2(self, emails: List[str]) -> int:
        import re
        for i, email in enumerate(emails):
            name = email[:email.find("@")]
            if "+" in name:
                name = name[:name.find("+")]
            if "." in name:
                name = "".join(name.split("."))
            emails[i] = name + email[email.rfind('@'):]
        return len(set(emails))

    def numUniqueEmails(self, emails: List[str]) -> int:
        for i, email in enumerate(emails):
            name, domen = email.split("@")
            if "+" in name:
                name = name[:name.find("+")]
            name = name.replace(".", "")
            emails[i] = name + "@" + domen
        return len(set(emails))


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
    print(Solution().numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
    print("--- %s seconds ---" % (time.time() - start_time))
