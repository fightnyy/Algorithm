#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);


    int a,b;
    while(cin>>a>>b){//So, if input a or b has any error then it cin's will be false or EOF also will be false without that
                     //it will be always True. So if input is not specified use like that.
        cout<<a+b<<'\n';
    }

}

/*
Can I use the following to check for end of input?

while(cin>>num1>>num2){
      // rest of code
}


Yes. It's not about what "cin returns", it about what it can become.

What happens in your while() is this:

1) The first operator>> extracts num1 from cin and returns (the modified) cin.
2) The second operator>> extracts num2 from cin and returns the (again modified) cin.
3) cin is converted to void* which gets converted to bool.

If there was an error or end-of-file was reached, cin will basically be converted to false, otherwise it will be true.

*/