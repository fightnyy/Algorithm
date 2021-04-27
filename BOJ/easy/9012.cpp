#include<iostream>
#include<stack>
using namespace std;


void solve()
{
    int num;
    int flag;
    cin>>num;
    while(num--)
    {
        string str;
        flag=1;
        stack<char>s;
        cin>>str;
        for(int i=0;i<str.length();i++){
            
            if(str[i]=='(')
            {
                s.push(str[i]);
            }
            else
            {
                if(!s.empty())
                s.pop();
                else
                {
                    cout<<"NO"<<"\n";
                    flag=0;
                    break;  //because I think that I should finish it in this fucntion so it makes me make another variable like flag
                            //So refer to the Code below, I don't have to finish this algoritm in this code I can use Main Fucntion.
                }
                
            }
        }
        if(flag==1){
        if(s.empty())
        cout<<"YES";
        else
        {
            cout<<"NO";
        }
        cout<<'\n';
        }
        
    }
}

int main()
{
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    solve();
}




// #include<iostream>
// #include<string>
// using namespace std;

// string valid(string s)
// {
//     int stack=0;
//     for (int i=0;i<s.length();i++)
//     {
//         if(s[i]=='(')
//         {
//             stack++;
//         }else
//         {
//             stack--;
//         }
//         if(stack<0)
//         return "NO";
        
//     }
//     if(stack==0)
//     {
//         return "YES";
//     }
//     else
//     {
//         return "NO";
//     }
    


// }

// int main()
// {
//     int t;
//     cin>>t;
//     while(t--)
//     {
//         string s;
//         cin>>s;
//         cout<<valid(s)<<'\n';
//     }
//     return 0;
// }