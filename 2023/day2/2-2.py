import re

total = 0
with open('2.txt') as f:
    for i, line in enumerate(f):
        line = line.split(':')[1]
        pattern = r"([0-9]+) (red|blue|green)"
        shows = line.split(';')
        blue, red, green = 0, 0, 0
        for show in shows:
            matches = re.findall(pattern, show)
            for match in matches:
                number, color = match
                if color == 'red':
                    red = max(int(number),red)
                elif color == 'blue':
                    blue = max(int(number),blue)
                elif color == 'green':
                    green = max(int(number),green)
        total += green * red * blue
print(total)
