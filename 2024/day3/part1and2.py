import re


pattern = "mul\(([0-9]+),([0-9]+)\)|(do\(\))|(don't\(\))"

with open('input.txt') as f:
    text = f.read()

matches = re.findall(pattern, text)

total=0

doing=True
for m in matches:
    if m[2]: #do
        doing=True
    if m[3]: #don't
        doing=False
    if doing and (m[0] and m[1]):
        total+=int(m[0])*int(m[1])
print(total)
