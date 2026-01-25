# 1.
with open('nums.txt', 'r') as f:
    with open('squared_numbers.txt', 'w') as f1:
        for line in f:
            num = int(line.strip())
            squared = num**2
            f1.write(str(squared))
            f1.write('\n')
            print(squared)

#2



