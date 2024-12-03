
reports = []
with open('input.txt') as f:
    for line in f.readlines():
        nums = [int(n) for n in line.strip().split(' ')]
        reports.append(nums)

def check(report):
    popped=False
    current = report[0]
    increasing = report[0] < report[1]
    for i,n in enumerate(report[1:]):
        diff = abs(current - n)
        if  diff > 3 or diff < 1:
            if popped:
                return 0
            else:
                popped = True
                report.pop(i+1)
                continue
        if increasing:
            if current > n:
                if popped:
                    return 0
                else:
                    popped = True
                    report.pop(i+1)
                    continue
        else: #decreasing
            if current < n:
                if popped:
                    return 0
                else:
                    popped = True
                    report.pop(i+1)
                    continue
        current = n
    return 1

correct = 0
for report in reports:
    c = check(report)
    print(c)
    correct+=c

print(correct)
