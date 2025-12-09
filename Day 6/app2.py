def index():
    with open("test.txt", "r") as f:
        ranges_input = f.read().splitlines()
    
    final_row = ranges_input[-1]          # last line as string


    ranges_input = [list(line) for line in ranges_input]


    # 1) Find operator positions
    col_starts = []
    operators = []

    for i, ch in enumerate(final_row):
        if ch in ["+", "*"]:
            col_starts.append(i)
            operators.append(ch)

    # 2) Build column ranges
    col_ranges = []

    for idx, start_col in enumerate(col_starts):
        
        if idx < len(col_starts) - 1:
            finish_col = col_starts[idx + 1] - 1
        else:
            finish_col = len(final_row) 
        col_ranges.append((start_col, finish_col))


    all_cols = []

    for (start_col, finish_col) in col_ranges:
        column_values = []

        for row in ranges_input[:-1]:
            slice_values = row[start_col : finish_col+1]
            digits = "".join(ch for ch in slice_values if ch.isdigit())
            if digits:
                column_values.append(int(digits))
                print(column_values)
            else: 
                column_values.append(None)
        all_cols.append(column_values)
    print("col values: ", all_cols)

    all_final_sums = []

    for final_index in range(len(all_cols)):
        col_number_val = all_cols[final_index]
        operator = operators[final_index]

        if operator == '*':
            sum = 1
        elif operator == '+':
            sum = 0
        
        for num in col_number_val:
            if operator == '*':
                sum = sum * num
            elif operator =='+':
                sum = sum + num
        
        all_final_sums.append(sum)
        print(all_final_sums)
    grand_total = 0

    for result in all_final_sums:
        grand_total = grand_total + result
        print(grand_total)

index()
