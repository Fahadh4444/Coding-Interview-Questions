// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
    public:
    // arr: input array
    // n: size of array
    //Function to find the sum of contiguous subarray with maximum sum.
    int maxSubarraySum(int arr[], int len){
        
        // Your code here
        int max_current=arr[0];
        int max_global=arr[0];
        
        for(int i=1; i<len; i++){
            max_current = (arr[i]>=(arr[i]+max_current))?arr[i]:(arr[i]+max_current);
            if(max_current > max_global){
                max_global = max_current;
            }
            // cout<<max_current<<":"<<max_global<<endl;
        }
        return max_global;
    }
};

// { Driver Code Starts.

int main()
{
    int n;
        
        cin>>n; //input size of array
        
        int a[n];
        
        for(int i=0;i<n;i++){
            cin>>a[i]; //inputting elements of array
    	}
            
        Solution ob;
        
        cout << ob.maxSubarraySum(a, n) << endl;

}
  // } Driver Code Ends
