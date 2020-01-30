# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]


class Account:
  def __init__(self, name, *emails):
    self.name = name
    self.emails = emails


class DSNode:
  pass

with open("prob.in", "r") as rf:
  # for line in open("prob.in")
  accounts = list(map(lambda line: Account(*line.split())))
  accounts = [Account(*line.split()) for line in rf]

print(map(lambda x: x*2, range(10)))


'''
2d grid 
some coords have obstacles

N = 5000

16 * 25M^2

2 robots, go to exit
commands: forward, right, left

'''
