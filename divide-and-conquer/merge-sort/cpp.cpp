#include <iostream>
using namespace std;

void merge(int nums[], int i, int k, int j){
    int first = i; // pin first element
    int temp_k = k+1;
    int c[j-i+1]; // temp list for sorted form
    int temp=0;
    while(temp_k <= j && i <= k){ // merge main part
        if(nums[i] <= nums[temp_k]){
            c[temp] = nums[i];
            temp++;
            i++;
        }
        else{
            c[temp] = nums[temp_k];
            temp_k++;
            temp++;
        }
    }
    // add element that remain from up
    for(i; i<=k; i++,temp++){
        c[temp]=nums[i];
    }
    for(temp_k; temp_k<=j; temp_k++, temp++){
        c[temp]=nums[temp_k];
    }
    // replace data in main list
    for(temp=0; first<=j; temp++,first++){
        nums[first]=c[temp];
    }
}

void merge_sort(int nums[], int i, int j){
    if(i==j)return;
    int k = (i+j)/2;
    // divide
    merge_sort(nums, i, k);
    merge_sort(nums, k+1, j);
    // merge
    merge(nums, i, k, j);
}

int main(){
    int n;
    cin>>n;
    int f=0, l=n-1;
    int numbers[n];
    for(int i=0; i<n; i++)cin>>numbers[i];
    merge_sort(numbers, f, l);

    for(int i=0; i<n; i++)cout<<numbers[i]<<' ';

    return 0;
}