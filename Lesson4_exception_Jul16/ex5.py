import random
item_in_shop = {"soybean_sauce": 0, "milk": 4, "salt": 10, "soybean_milk": 3}
items = [item for item in item_in_shop.keys()]
cnt = 5

def buy(item):
    if item == 'soybean_sauce':
        raise Exception("I didn't buy anything")
    if item != 'soybean_sauce': 
        print("Mommy! I've bought {} for you!".format(item))

# 買五個隨機的東西
while cnt:
    cnt -= 1
    index = random.randint(0,3)
    item = items[index]
    try:
        buy(item)
    except Exception as e:
        print(e)