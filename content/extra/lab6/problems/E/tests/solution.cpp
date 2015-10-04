#include<iostream>
#include<cmath>

using namespace std;

double dist(double x1, double y1, double x2, double y2)
{
	return ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}


int main()
{
	double x1, y1, x2, y2, r;
	cin>>x1>>y1>>x2>>y2>>r;
	cout<<((dist(x1,y1,x2,y2)<=r*r)?"YES":"NO")<<endl;
	return 0;
}

