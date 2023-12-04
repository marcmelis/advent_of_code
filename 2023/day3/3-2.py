total = 0
with open('3.txt') as f:
    text = f.readlines()
    for line_index, line in enumerate(text):
        gears = [i for i, character in enumerate(line) if character == '*']
        for gear in gears:
            numbers = []
            # *****
            # -123-
            # -----
            if line_index != 0:
                gear_upper = [num for num in range(gear-1,gear+2) if num >= 0 and num < len(line)]
                numbers += ([
                    num for start, end, num in intervals[line_index - 1]
                    if any(g in range(start, end) for g in gear_upper)
                ])
            # -----
            # -123-
            # *****
            if line_index + 1 != len(text):
                gear_lower = [num for num in range(gear-1,gear+2) if num >= 0 and num < len(line)]
                numbers += ([
                    num for start, end, num in intervals[line_index + 1]
                    if any(g in range(start, end) for g in gear_upper)
                ])
            # -----
            # *123*
            # -----
            if gear != 0:
                numbers += ([
                    num for start, end, num in intervals[line_index]
                    if end == gear
                ])
            if gear + 1 != len(line):
                numbers += ([
                    num for start, end, num in intervals[line_index]
                    if start == gear +1
                ])

            if len(numbers) == 2:
                total += int(numbers[0]) * int(numbers[1])
    print(total)
