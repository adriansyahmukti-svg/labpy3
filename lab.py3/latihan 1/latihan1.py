from random import random
n = int(input("masukan nilai n:"))
i = 0
while i < n:
    for j in range(5):
        a = random()
        if a < 0.5:
            print(f"data ke: {i+1} => {a}")
            i += 1
            print("selesai")        