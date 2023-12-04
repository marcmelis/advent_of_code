total = 0
with open('4.txt') as f:
    repetitions = [1 for i in range(len(f.readlines()))]
with open('4.txt') as f:
    for i, line in enumerate(f):
        winning, numbers = line.split('|')
        winning =  [n for n in winning.strip().split(' ') if n != ""]
        numbers = [n for n in numbers.strip().split(' ') if n != ""]
        winners = [n for n in numbers if n in winning]
        for j in range(i+1, i+len(winners)+1):
            if j < len(repetitions):
                repetitions[j] += repetitions[i]
print(sum(repetitions))
