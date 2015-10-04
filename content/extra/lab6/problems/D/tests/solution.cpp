#include<iostream>

using namespace std;

bool test(double x, double y)
{
	return x+y<=1 && x+y>=-1 && x-y<=1 && x-y>=-1;
}

int main()
{
	double x, y;
	cin>>x>>y;
	cout<< (test(x,y)?"YES":"NO") <<endl;
	return 0;
}

