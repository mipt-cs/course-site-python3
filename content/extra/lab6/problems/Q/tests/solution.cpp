#include<iostream>
using namespace std;

double pow(double a, int n)
{
    if (n==0)
	return 1;
    else
        return a*pow(a,n-1);
}

int main()
{
	double a;
	int n;
	cin>>a>>n;
	cout<<pow(a,n)<<endl;
	return 0;
}
