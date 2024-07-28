#include <bits/stdc++.h>
using namespace std;
int sum(int a, int b){
  return a+b;
}
int main() 
{
  pair<int,int> p={1,3};
  cout<<p.first<<" "<<p.second<<endl;
  pair<int,int> arr[]={{4,3},{5,6}};
  for(auto it: arr) cout<<it.first<<" "<<it.second<<" ";
  int c=sum(5,6);
  cout << endl<<"Hello, World!"<<c;
  return 0;
}
