def index():
    with open("data.txt", "r") as f:
        ranges_input = f.read().splitlines()

    try:
        limiter_index = ranges_input.index("")
    except ValueError:
        print("no blank space fix ya code")
    else:
        freshrange = ranges_input[:limiter_index]
        ingredientID = ranges_input[limiter_index +1:]
    
    print(freshrange, ingredientID)

    countfresh = 0
    uniqueNumber =[]

    for items in freshrange:
        splitrange = items.index("-")
        lowerrange= items[:splitrange]
        upperrange= items[splitrange +1:]
        for ingreditent in ingredientID:
            print("checking", ingreditent, "in range of", lowerrange, "-", upperrange)
            if int(lowerrange) <= int(ingreditent) <= int(upperrange):
                print("this item is fresh af", ingreditent)
                if ingreditent not in uniqueNumber:
                    uniqueNumber.append(ingreditent)
                    print(uniqueNumber)
                    countfresh +=1
                
            

    print(countfresh)

index()