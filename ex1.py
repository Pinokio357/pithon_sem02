from random import  randint
coin_count = int(input("enter coin number: "))
zero_side = 0
number_side = 0
for i in range(coin_count):
    coin_side = randint(0, 1)
    print(coin_side, end = ", ")
    if coin_side == 0:
        zero_side += 1
    else :
        number_side += 1

print("\n","minimal turn over count:{}".format(zero_side if zero_side < number_side else number_side))