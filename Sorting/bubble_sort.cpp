#include<bits/stdc++.h>
using namespace std;
int main(){
   int N = 6;
   int arr[N] = {13,46,24,52,20,9};

   for (int i=N-1; i>=0; i--)
   {
       for (int j=1; j<N; j++)
       {
           if (arr[j] < arr[j-1])
           {
             swap(arr[j-1] , arr[j]);
           }
       }
   }

   for (int i=0; i<N; i++)
   {
       cout<<arr[i]<<" ";
   }
   
    return 0;
}