import re

total = 0
seeds = []
trans_dicts = [
    {}, # seed-to-soil map
    {}, # soil-to-fertilizer map
    {}, # fertilizer-to-water map
    {}, # water-to-light map
    {}, # light-to-temperature map
    {}, # temperature-to-humidity map
    {}, # humidity-to-location map
]
with open('day5/5.txt') as f:
    part = -1
    for line in f:
        if line.startswith('seeds:'):
            seeds = list(map(int,re.findall('[0-9]+', line)))
        elif line.startswith('seed-to'):
            part=0
        elif line.startswith('soil-to'):
            part=1
        elif line.startswith('fertilizer-to'):
            part=2
        elif line.startswith('water-to'):
            part=3
        elif line.startswith('light-to'):
            part=4
        elif line.startswith('temperature-to'):
            part=5
        elif line.startswith('humidity-to'):
            part=6
        else:
            if line != '\n':
                destination, origin, length = map(int,line.split(' '))
                trans_dicts[part][(origin,origin+length)] = destination

def find_transition(seed, transition_dict):
    for origin, destination in transition_dict.items():
        start, end = origin
        if seed >= start and seed < end:
            return seed - start + destination
    return seed

min_seed = float('inf')
for seed in seeds:
    for transition_dict in trans_dicts:
        seed = find_transition(seed, transition_dict)
    min_seed = min(seed,min_seed)
print(min_seed)
