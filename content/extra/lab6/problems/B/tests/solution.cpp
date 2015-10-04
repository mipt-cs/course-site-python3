#include<iostream>
#include<cmath>

using namespace std;

double dist(double x1, double y1, double x2, double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main()
{
	double x1, y1, x2, y2;
	cin>>x1>>y1>>x2>>y2;
	cout<<dist(x1,y1,x2,y2)<<endl;
	return 0;
}

