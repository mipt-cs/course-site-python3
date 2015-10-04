#include<iostream>

using namespace std;

void simplify(int & a, int & b)
{
    for(int i=a; i>1;--i)
    {
	    if(a%i==0 && b%i==0)
	    {
		    a/=i;
		    b/=i;
		    return;
	    }
    }
}

int main()
{
	int a, b;
	cin>>a>>b;
	simplify(a,b);
	cout<<a<<" "<<b<<endl;
	return 0;
}

