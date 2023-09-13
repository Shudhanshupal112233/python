import random
# random.seed(10)
# print(random.random())
# random.seed(10)
# print(random.seed(10))
# print(random.randrange(1,13,2))
# x="welocme"
# print(random.choice(x))
import random
randomlist = []
for i in range(0,5):
  n = random.randrange(1,30,5)
  randomlist.append(n)
print(randomlist)
