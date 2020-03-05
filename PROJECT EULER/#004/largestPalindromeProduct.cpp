#include <iostream>
using namespace std;

bool isPalindrome(int);

int main(){
  int t, n, big;
  cin>>t;
  for(int i = 0; i < t; i++){
    cin>>n;
    big = 0;
    for(int j = 100; j < 1000; j++)
      for(int k = 100; k < 1000; k++)
        if (isPalindrome(j*k) && j*k < n)
          if (j*k > big)
            big = j*k;
    cout<<big<<"\n";
  }
  return 0;
}

bool isPalindrome(int n){
  int copy = n, rev = 0;
  while(n > 0){
    rev = (rev*10)+(n%10);
    n /= 10;
  }
  return rev == copy;
}
