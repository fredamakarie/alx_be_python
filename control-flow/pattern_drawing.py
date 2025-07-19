pattern_size = int(input("Enter the size of the pattern: "))
unit = "+"
counter  = 0

#for i in range(pattern_size):
while counter < pattern_size:
    print(unit * pattern_size)
    counter += 1