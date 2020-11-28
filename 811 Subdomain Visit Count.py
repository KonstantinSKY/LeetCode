"""811. Subdomain Visit Count https://leetcode.com/problems/subdomain-visit-count/ """

import time
from typing import List


class Solution:
    def subdomainVisits2(self, cpdomains: List[str]) -> List[str]:
        domains = {}
        for cp in cpdomains:
            cp_list = cp.split()
            domain_list = cp_list[1].split(".")
            for i in range(len(domain_list)):
                domain = ".".join(domain_list[i:])
                if domain not in domains:
                    domains.update({domain: 0})
                domains[domain] += int(cp_list[0])
                print(domains)
        return [str(domains[v])+" "+v for v in domains]


    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict
        domains = defaultdict(int)
        for cp in cpdomains:
            count, s = cp.split()
            count = int(count)
            pos = s.find(".")
            while pos > 0:
                domains[s] += count
                pos = s.find(".")
                s = s[pos+1:]
        return [str(domains[v])+" "+v for v in domains]


if __name__ == "__main__":
    start_time = time.time()
    print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
    print(Solution().subdomainVisits(["9001 discuss.leetcode.com"]))

    print("--- %s seconds ---" % (time.time() - start_time))
