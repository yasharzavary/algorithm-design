#include <iostream>
using namespace std;


int place(int nums[], int i, int j){
    int first = i;
    int swap_temp;
    int last = j;
    // until finding the true point go
    while(true){
        // going until reach place
        while(i <= last && nums[first] >= nums[i])i++;
        while(nums[j] > nums[first])j--;
        // replacing part(depend on i and j)
        if(i >= j){
            swap_temp = nums[first];
            nums[first] = nums[j];
            nums[j] = swap_temp;
            return j;
        }
        swap_temp = nums[i];
        nums[i] = nums[j];
        nums[j] = swap_temp;
    }

}

void quick_sort(int nums[], int i, int j, int n){
    if(j<=i)return; // return when we reach one or zero element
    int temp = place(nums, i, j); // find place of candidate element
    // sort left and right part
    quick_sort(nums, i, temp-1, n);
    quick_sort(nums, temp+1, j, n);
}

int main(){
    int n;
    cin>>n;
    int number_list[n];

    for(int i=0; i<n; i++)cin>>number_list[i];
    quick_sort(number_list, 0, n-1, n);
    for(int i=0; i<n; i++)cout<<number_list[i]<<' ';


    return 0;
}