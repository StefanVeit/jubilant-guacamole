import random
import sys

n = int(sys.argv[1])
b = []
for i in range(1,n):
    a = random.randint(1,6)
    b.append(a)

c = sum(b)

average = c/n

print('Durschnittliche Würfelzahl:',average)
