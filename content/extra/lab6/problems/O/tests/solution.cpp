#include<iostream>
using namespace std;
int main()
{
	int sum=0,n=0;
	do
	{
		cin>>n;
		sum+=n;
	}
	while(n!=0);
	cout<<sum<<endl;
	return 0;
}
