
reports = []
with open('input.txt') as f:
    for line in f.readlines():
        nums = [int(n) for n in line.strip().split(' ')]
        reports.append(nums)

def check(report):
    current = report[0]
    increasing = report[0] < report[1]
    for n in report[1:]:
        diff = abs(current - n)
        if  diff > 3 or diff < 1:
            return 0
        if increasing:
            if current > n:
                return 0
        else: #decreasing
            if current < n:
                return 0
        current = n
    return 1

correct = 0
for report in reports:
    correct+=check(report)

print(correct)
