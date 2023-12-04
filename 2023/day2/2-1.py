import re
max_green = 13
max_blue = 14
max_red = 12

sum_ids = 0
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
        if blue <= max_blue and red <= max_red and green <= max_green:
            sum_ids+= i+1
print(sum_ids)
