pattern_size = int(input("Enter the size of the pattern: "))
counter  = 0

#for i in range(pattern_size):
#while counter < pattern_size:
    #print (pattern_size * "*", end="\n")
    #counter += 1

while counter < pattern_size: 
    j=0
    while j < pattern_size:
        print ("*", end="")
        j+=1
    print()
    counter += 1
