#include<iostream>
#include<vector>
#include<stack>

using namespace std;

void solve()
{
    int num;
    cin>>num;//when use cin remember that buffer retain enter only in (cin+getline)
            //cin with for loop don't care
    cin.ignore();
    
    for(int i=0;i<num;i++)
    {  
        string a;
        getline(cin,a);
        a+='\n';
        
        for(int j=0;j<=a.length();j++)
        {
            stack<char>s;// because of stack location waste time about an hour.......  what is the counter example. 
                        //that the location of the stack should be located in here except forced terminatnion
                        //so when you think everything is fine. you should check about the location of varialbes 
            if(a[j]==' '||a[j]=='\n')
            {
               while(!s.empty())
               { 
                   cout<<s.top();
                   s.pop();
               }
               cout<<a[j];
            }
            else
            {
                 s.push(a[j]);
            }
        }
            
    }
    
}
int main()
{
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    solve();
    return 0;
}