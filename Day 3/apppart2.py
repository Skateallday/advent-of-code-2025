
def getmax(line, maxlen):
    remove = len(line) - maxlen
    stack = []

    for d in line:
        while remove > 0 and stack and stack [-1] <d:
            stack.pop()
            remove -=1

        stack.append(d)
    return ''.join(stack[:maxlen])

def index(maxlen):
    total = 0
    with open("data.txt", "r") as f:
        data = f.read().strip()
    
        newlist = data.split( '\n')

        for items in newlist:   
            number = getmax(items, maxlen)
            total += int(number)
    print(total)

index(12)