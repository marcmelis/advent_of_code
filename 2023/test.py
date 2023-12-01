import re
text='eightwo'
pattern='(one|two|three|four|five|six|seven|eight|nine|zero|1|2|3|4|5|6|7|8|9|0)'
re_sult = re.findall(pattern,text)
num_dict = { 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight':'8', 'nine': '9', 'zero': '0'}
first = re_sult[0]
last = re_sult[-1]
if not first.isnumeric():
    first = num_dict[first]
if not last.isnumeric():
    last = num_dict[last]

print(first + last)
