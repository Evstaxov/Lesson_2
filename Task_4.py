string = (input("Enter the numbers with space - ")).split()
print(string)

for i in range(len(string)):
    if len(string[i]) <= 10:
        print(i, string[i])
    else:
        print(i, (string[i])[:10])