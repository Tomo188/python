import random
auta = ["ford", "mercedes", "audi", "ford"]
coin = random.choices(["tails", "heads"], weights=[2, 1], k=23)
random.seed(2)
print(random.randint(100, 200))
