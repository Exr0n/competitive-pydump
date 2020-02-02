# https://leetcode.com/problems/accounts-merge

# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], [
#     "John", "john_newyork@mail.com", "johnsmith@mail.com", "johnsmith_newyork@mail.com"], ["Mary", "mary@mail.com"]]

accounts = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"], [
    "David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"], ["David", "David1@m.co", "David2@m.co"]]


class Solution:
    def accountsMerge(self, accounts):
        node_by_email = {}

        class DSNode:
            @staticmethod
            def merge(a: str, b: str):
                if (node_by_email[a].size < node_by_email[b].size):
                    node_by_email[b].size += node_by_email[a].size
                    node_by_email[node_by_email[a].father].father = node_by_email[b].father
                else:
                    node_by_email[a].size += node_by_email[b].size
                    node_by_email[node_by_email[b].father].father = node_by_email[a].father
            
            def __init__(self, email: str, father: str, name: str, size: int = 1):
                self.email = email
                self.father = father
                self.name = name
                self.size = size

            @property
            def father(self):
                if self.email != self.__father:
                    self.__father = node_by_email[self.__father].father
                return self.__father

            @father.setter
            def father(self, name: str):
                self.__father = name

            @property
            def size(self):
                if (self.__father == self.email):
                    return self.__size
                return node_by_email[self.father].size

            @size.setter
            def size(self, size: int):
                self.__size = size

            def __repr__(self):
                return 'DSNode({}, {}->{})'.format(self.name, self.email, self.father)
            
        class Account:
            def __init__(self, name: str, do_sort: bool = True):
                self.name = name
                self.do_sort = do_sort
                self.emails = []
            
            

        for acct in accounts:
            for email in acct[1:]:
                if email in node_by_email:
                    # FIX: need double layer because we need to set the
                    # father of the father of the first email in this account
                    # instead of just the father of the first email
                    DSNode.merge(acct[1], email)
                else:
                    node_by_email[email] = DSNode(email, acct[1], acct[0])

        out = {}
        for email in node_by_email:
            account_email = node_by_email[email].father
            if not account_email in out:
                out[account_email] = Account(node_by_email[email].name)
            out[account_email].emails.append(email)

        return [[account.name] + sorted(account.emails) for account in out.values()]


if __name__ == "__main__":
    sol = Solution()
    print(sol.accountsMerge(accounts))
