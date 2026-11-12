import time

n = int(input("Entrer un nombre : "))

for i in range(n, -1, -1):
    print(i, flush=True)
    time.sleep(1)

while n != -1:
    print(n, flush=True)
    time.sleep(1)
    n-=1