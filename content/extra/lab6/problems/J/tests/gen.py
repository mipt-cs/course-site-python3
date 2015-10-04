import sys

def isprime(n):
    if n==2:
		return 1

    if n%2==0:
		return 0

    j=3
    while j*j<=n:
		if n%j==0:
			return 0
		j+=2
    return 1

n=31000

while ( not isprime(n) ):
	n=n+1

print n*n
