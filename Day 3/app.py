def index():
    with open("data.txt", "r") as f:
        data = f.read().strip()

    totaljoltage = 0
    
    newlist = data.split( '\n')

    for items in newlist:     
        a = 0
        b = 0
        for item in items[:-1]:

            if int(item) > int(a):
                
                a = item
        idx = items.index(a)
        afterblist = items[idx +1:]

        for bitems in afterblist:  
            if int(bitems) > int(b):
                b = bitems


        totaljoltage += int((str(a) + str(b)))

    print(f"total joltage is {totaljoltage}")

index()