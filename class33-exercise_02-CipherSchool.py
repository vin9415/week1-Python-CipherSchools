## problem 
# ask user a number conntaining more than one digit 
# example - 1256
# calculate 1+2+5+6 and print
n = input("")
total = 0
i = 0
while i < len(n):
    total += int(n[i])
    i += 1
print(total)    





