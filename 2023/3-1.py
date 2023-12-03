import re
pattern = '[0-9]+'
symbols = ['$','*','#','+','=','@','/','%','&', '-']
total = 0
with open('data/3-1.txt') as f:
    text = f.readlines()
    for i, line in enumerate(text):
        re_sult = re.findall(pattern,line)
        intervals = [(m.start(0), m.end(0), m.group(0)) for m in re.finditer(pattern, line)]
        for interval in intervals:
            start, end, number = interval
            if start != 0:
                start-= 1
            if end - 1 != len(line):
                end+= 1
            # Check line above for symbols
            # *****
            # -123-
            # -----
            above = (i != 0 and any(s in text[i-1][start:end] for s in symbols))
            # If not found check line below
            # -----
            # -123-
            # *****
            below = (i+1 != len(text) and any(s in text[i+1][start:end] for s in symbols))
            # Check the borders on that same line
            # -----
            # *123*
            # -----
            left_side = start-1 != 0 and line[start] in symbols
            right_side = end != len(line) - 1 and line[end-1] in symbols
            if (above or below or left_side or right_side):
                total+=int(number)
    print(total) 
