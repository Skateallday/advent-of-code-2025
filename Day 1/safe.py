
def index():
    begin = 50

    with open('data.txt', 'r') as f:
        array = [line.strip() for line in f if line.strip()]

    zeros = 0

    for item in array:
        direction = item[0]
        value = int(item[1:])
        start = begin

        if direction == "R":
            end = (start + value) % 100
            if start < end:
                zeros_during = 0  
            else:
                zeros_during = 1 
        else: 
            end = (start - value) % 100
            if start > end:
                zeros_during = 0
            else:
                zeros_during = 1

        zeros += zeros_during
        if end == 0 and zeros_during == 0:
            zeros += 1

        begin = end

    print("Final dial position:", begin)
    print("Password (total zeros):", zeros)

index()