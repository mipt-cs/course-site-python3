#include<iostream>

using namespace std;


int sum(int a, int b)
{
	if(b==0)
		return a;
	else
		return sum(a+1, b-1);
}

int main()
{
	int a, b;
	cin>>a>>b;
	cout<<sum(a,b)<<endl;
	return 0;

}
