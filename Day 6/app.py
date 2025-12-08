def index():
    with open("data.txt", "r") as f:
        ranges_input = f.read().splitlines()

    print(ranges_input)
index()