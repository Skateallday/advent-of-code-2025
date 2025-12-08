def is_repeated_pattern(s: str) -> bool:
    # True if s is made of a smaller substring repeated (length >= 2)
    return s in (s + s)[1:-1]


with open("data.txt", "r") as f:
    ranges_input = f.read().strip()

total_invalid = 0
range_list = ranges_input.split(",")

for range_str in range_list:
    start_str, end_str = range_str.split("-")
    start = int(start_str)
    end = int(end_str)

    for num in range(start, end + 1):
        s = str(num)

        # Check if entire number is a repeated pattern
        if is_repeated_pattern(s):
            total_invalid += num

print("Total value of invalid IDs:", total_invalid)
