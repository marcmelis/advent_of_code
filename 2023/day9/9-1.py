import re
with open('9.txt') as f:
    total = 0
    for line in f:
        seq = list(map(int,re.findall('-?[0-9]+',line)))
        all_zeros=False
        sequences = [seq]
        current_seq_i = 0
        while not all_zeros:
            new_seq = []
            current_seq = sequences[current_seq_i]
            for i, num in enumerate(current_seq):
                if i + 1 == len(current_seq): continue
                new_seq.append(current_seq[i+1]-current_seq[i])
            sequences.append(new_seq)
            current_seq_i +=1
            if all([num == 0 for num in new_seq]):
                all_zeros = True
        final_num = 0
        for seq in sequences:
            final_num += seq[-1]
        total+=final_num
    print(total)
