#pracice for loop
# ask user a number like 1256
# calculate sum of digits

total = 0
num = input("Enter a number: ")
for i in range(0,len(num)):
    total += int(num[i])
print(total)