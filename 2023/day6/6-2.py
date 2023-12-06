# Not good
with open('6.txt') as f:
    time, distance = f.readlines()
    time = int(time.split(':')[1].strip().replace(' ',''))
    record_distance = int(distance.split(':')[1].strip().replace(' ',''))
    wins = 0
    for i in range(time+1):
        distance = i *(time - i)
        if distance > record_distance: wins += 1
    print(wins)
