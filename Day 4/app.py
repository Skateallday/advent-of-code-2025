def index():
    with open("data.txt", "r") as f:
        ranges_input = f.read().splitlines()
    
    row = len(ranges_input)
    col = len(ranges_input[0])

    accessibleCount = 0

    ranges_input = [list(line) for line in ranges_input]

    while True:
        changed = False

        for index, items in enumerate(ranges_input):
            previousline = ranges_input[index - 1] if index > 0 else None
            nextline = ranges_input[index + 1] if index < row - 1 else None

    
            for col_index in range(col):
                if items[col_index] != "@":
                    continue

                count = 0
                if col_index > 0 and items[col_index - 1] == "@":
                    count += 1
                    print(f"Hit left, count = {count}")

                if col_index < col - 1 and items[col_index + 1] =="@":
                    count += 1                
                    print(f'hit right, count = {count} ')

                if previousline:
                    if col_index > 0 and previousline[col_index - 1] == "@":
                        count +=1 
                    if previousline[col_index] == "@":
                        count +=1
                    if col_index < col - 1 and previousline[col_index +1 ] == "@":
                        count +=1 

                if nextline:
                    if col_index > 0 and nextline[col_index - 1] == "@":
                        count +=1 
                    if nextline[col_index] == "@":
                        count +=1
                    if col_index < col - 1 and nextline[col_index +1 ] == "@":
                        count +=1   

                            

                if count < 4:
                    items[col_index] = "."
                    accessibleCount +=1 
                    changed = True
                    print(f"Accessible roll at ({index}, {col_index}), total accessible = {accessibleCount}")
        if not changed:
            break
        
        
    print("total accessible", accessibleCount)
    
    return accessibleCount      

index()