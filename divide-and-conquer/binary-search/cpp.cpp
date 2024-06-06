
#include <iostream>
using  namespace  std;

int search(int target, int number_arr[], int i, int j){
    if(j < i)return -1; // condition of not finding the number in list
    int temp = (i + j)/2;
    // checking and guessing place of the target element
    if (number_arr[temp] == target) return temp;
    else if(number_arr[temp] > target)return search(target, number_arr, i, temp-1);
    else return search(target, number_arr, temp+1, j);
}

int main(){
    int n, t;
    cin>>n;
    int arr[n];

    // get number of number_list and search the target in it
    for(int i=0; i<n; i++)cin>>arr[i];
    cin>>t;
    cout<<search(t, arr, 0, n-1);

    return 0;
}
