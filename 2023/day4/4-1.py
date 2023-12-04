total = 0
with open('data/4.txt') as f:
    for line in f:
        winning, numbers = line.split('|')
        winning =  [n for n in winning.strip().split(' ') if n != ""]
        numbers = [n for n in numbers.strip().split(' ') if n != ""]
        winners = [n for n in numbers if n in winning]
        if winners:
            total+=2**(len(winners) -1)
print(total)
