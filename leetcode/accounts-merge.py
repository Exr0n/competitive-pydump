accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "john_newyork@mail.com", "johnsmith@mail.com", "johnsmith_newyork@mail.com"], ["Mary", "mary@mail.com"]]

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


# class Account:
#     def __init__(self, name, *emails):
#         self.name = name
#         self.emails = emails
#
# with open("prob.in", "r") as rf:
#     # for line in open("prob.in")
#     accounts = list(map(lambda line: Account(*line.split())))
#     accounts = [Account(*line.split()) for line in rf]
#     for acct in accounts:
#         for email in emails:
#             emails[email] = DSNode(email, acct.emails[0], acct.name)

for acct in accounts:
    for email in acct[1:]:
        if email in emails:
            emails[acct[1]].father = emails[email].father
        else:
            emails[email] = DSNode(email, acct[1], acct[0])

out = {}
for email in emails:
    acct_email = emails[email].father
    if not acct_email in out:
        out[acct_email] = [emails[email].name]
    out[acct_email].append(email)

ret = [[acct[0]] + sorted(acct[1:]) for acct in out.values()]
print(ret)
