fin = open('input.txt')
N = int(fin.readline())
sales = [int(nominal) for nominal in fin.readline().split()]

counter = 0
coins_needed = 0
for sale in sales:
    if sale == 5:
        counter -= 1
    else:
        counter += sale//5 - 1
    if counter > coins_needed:
        coins_needed = counter

fout = open('output.txt', 'w')
print(coins_needed, file = fout)
fout.close()
