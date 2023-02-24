sum = int(input("enter  sum number: "))
mult = int(input("enter mult number: "))

for i in range(sum):
    for j in range(mult):
        if sum == i + j and mult == i * j:
            print(f"numbers are: {i}, {j}")



