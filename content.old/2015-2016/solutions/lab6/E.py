fin = open('input.txt')
N, K = fin.readline().split()
gentleman_number = int(N)
deals_number = int(K)

gentleman_balance = [0]*(gentleman_number + 1) # 0 is fictive gentleman

for i in range(deals_number):
    deal = fin.readline()
    debitor, creditor, cash = [int(x) for x in deal.split()]
    gentleman_balance[debitor] -= cash
    gentleman_balance[creditor] += cash

fout = open('output.txt', 'w')
print(*gentleman_balance[1:], file = fout)
fout.close()
