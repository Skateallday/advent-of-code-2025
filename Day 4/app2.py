def index(default_value=None):
    
    with open("test.txt", "r") as f:
        ranges_input = f.read().splitlines()
        
    rows = len(ranges_input)
    cols = len(ranges_input[0])

    accessible_count = 0
    overall_count = 0

    for row_index, items in enumerate(ranges_input):
        previous_line = ranges_input[row_index - 1] if row_index > 0 else None
        next_line = ranges_input[row_index + 1] if row_index < rows - 1 else None

        for col_index in range(cols):
            if items[col_index] != "@":
                print("Move on")
                continue

            count = 0
            print(f"\nChecking row {row_index}, col {col_index}")

            # Left
            if col_index > 0 and items[col_index - 1] == "@":
                count += 1
                print(f"Hit left, count = {count}")

            # Right
            if col_index < cols - 1 and items[col_index + 1] == "@":
                count += 1
                print(f"Hit right, count = {count}")

            # Above row
            if previous_line:
                if col_index > 0 and previous_line[col_index - 1] == "@":
                    count += 1
                    print(f"Hit up-left, count = {count}")
                if previous_line[col_index] == "@":
                    count += 1
                    print(f"Hit up, count = {count}")
                if col_index < cols - 1 and previous_line[col_index + 1] == "@":
                    count += 1
                    print(f"Hit up-right, count = {count}")

            # Below row
            if next_line:
                if col_index > 0 and next_line[col_index - 1] == "@":
                    count += 1
                    print(f"Hit down-left, count = {count}")
                if next_line[col_index] == "@":
                    count += 1
                    print(f"Hit down, count = {count}")
                if col_index < cols - 1 and next_line[col_index + 1] == "@":
                    count += 1
                    print(f"Hit down-right, count = {count}")

            # Check accessibility
            if count < 4:
                accessible_count += 1
                print(f"Accessible roll at ({row_index}, {col_index}), total accessible = {accessible_count}")
            else:
                print("Not accessible")
        overall_count = overall_count + accessible_count
        print(f"overall count is {overall_count}")

    return accessible_count

index()