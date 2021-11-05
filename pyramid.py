rows = int(input("Enter the number of rows: "))
for row in range (0, rows):
    for _ in range(0, rows-row-1):
        print(end=' ')
    for _ in range(0, row+1):
        print('x', end=' ')
    print(' ')