def index():
    with open("data.txt", "r") as f:
        lines = [line.strip() for line in f]

    # Try to find the blank line separator
    try:
        limiter_index = lines.index("")
        freshrange = lines[:limiter_index]
    except ValueError:
        print("no blank space fix ya code")
        freshrange = lines  # or just use all lines if no blank

    intervals = []

    for line in freshrange:
        if not line:
            continue

        try:
            left, right = line.split("-", 1)
            low = int(left)
            high = int(right)

            # Normalise in case someone writes "high-low" backwards
            if high < low:
                low, high = high, low

            intervals.append((low, high))
        except ValueError:
            print(f"Skipping bad line: {line!r}")
            continue

    if not intervals:
        print(0)
        return

    # Sort by start of range
    intervals.sort(key=lambda x: x[0])

    # Merge overlapping or touching intervals
    merged = []
    cur_start, cur_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= cur_end + 1:
            # Overlaps or is directly adjacent – extend current interval
            cur_end = max(cur_end, end)
        else:
            # No overlap – push current and start a new one
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))

    # Sum the lengths of merged intervals
    total_unique = sum(end - start + 1 for start, end in merged)
    print(total_unique)


index()
