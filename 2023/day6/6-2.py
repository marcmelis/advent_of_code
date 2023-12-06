with open('6.txt') as f:
    time, distance = f.readlines()
    t = int(time.split(':')[1].strip().replace(' ',''))
    D = int(distance.split(':')[1].strip().replace(' ',''))
    limit1 = (-t + (t**2-(4*D))**0.5) / -2
    limit2 = (-t - (t**2-(4*D))**0.5) / -2
    if limit1 == int(limit1): limit1 += 1
    print(int(limit2)-int(limit1))
