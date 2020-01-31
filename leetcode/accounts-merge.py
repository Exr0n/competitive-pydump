# https://leetcode.com/problems/accounts-merge
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], [
#     "John", "john_newyork@mail.com", "johnsmith@mail.com", "johnsmith_newyork@mail.com"], ["Mary", "mary@mail.com"]]

accounts = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"], [
    "David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"], ["David", "David1@m.co", "David2@m.co"]]


class Solution:
    def accountsMerge(self, accounts):
        emails = {}

        class DSNode:

            def __init__(self, email: str, father: str, name: str):
                self.email = email
                self.father = father
                self.name = name

            @property
            def father(self):
                if self.email != self.__father:
                    self.__father = emails[self.__father].father
                return self.__father

            @father.setter
            def father(self, name: str):
                self.__father = name

            def __repr__(self):
                return 'DSNode({}, {}->{})'.format(self.name, self.email, self.father)

        for acct in accounts:
            for email in acct[1:]:
                if email in emails:
                    # FIX: need double layer because we need to set the
                    # father of the father of the first email in this account
                    # instead of just the father of the first email
                    emails[emails[acct[1]].father].father = emails[email].father
                else:
                    emails[email] = DSNode(email, acct[1], acct[0])

        out = {}
        for email in emails:
            acct_email = emails[email].father
            if not acct_email in out:
                out[acct_email] = [emails[email].name]
            out[acct_email].append(email)

        return [[acct[0]] + sorted(acct[1:]) for acct in out.values()]


if __name__ == "__main__":
    sol = Solution()
    print(sol.accountsMerge(accounts))
