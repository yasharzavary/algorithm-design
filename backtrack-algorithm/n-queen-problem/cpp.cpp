#include <iostream>
using  namespace  std;

bool validator(int i, int arr[]){
    if(i==0 || i==1)return true;
    i--;
    for(int j=0; j<i; j++){
        if((arr[j] == arr[i]) || (abs(j - i) == abs(arr[j] - arr[i])))return false;
    }
    return true;
}

int solve(int n, int arr[], int i=0){
    if(validator(i, arr)){
        if(i==n)return n;
        for(int j=0; j<n; j++){
            arr[i] = j;
            int find;
            find = solve(n, arr, i+1);
            if(find == n)return n;
        }

    }
    return -1;
}


int main(){
    int n;
    cin>>n;
    int queens[n];
    if(solve(n, queens) == -1)cout<<-1;
    else for(int i = 0; i<n; i++)cout<<queens[i]<<' ';


    return 0;
}