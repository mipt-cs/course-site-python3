#include<iostream>
using namespace std;

int fib(int n)
{
    if (n==0 || n==1)
	return n;
    else
        return fib(n-1)+fib(n-2);
}

int main()
{
	int n, k;
	cin>>n;
	cout<<fib(n)<<endl;
	return 0;
}
