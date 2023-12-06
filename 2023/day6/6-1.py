import re
with open('6.txt') as f:
    time, distance = f.readlines()
    races = list(zip(map(int,re.findall('[0-9]+',time)),map(int,re.findall('[0-9]+',distance))))

total = 1
for race in races:
    max_time, record_distance = race
    wins = 0
    for time_button in range(max_time+1):
        distance = time_button *(max_time - time_button)
        if distance > record_distance: wins += 1
    total *= wins
print(total)
