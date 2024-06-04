#include <iostream>
using namespace std;


void solve(int k, int n, int number_list[], int temp[], int i=0)
{
    if(k == 0){
        for(int j=0; j<i; j++){
            cout<<temp[j]<<' ';
        }
        cout<<endl;
        return;
    }
    else if(k < 0)return;
    else if(n == -1)return;
    solve(k, n-1, number_list, temp, i);
    temp[i] = number_list[n];
    solve(k - number_list[n], n-1, number_list, temp, i+1);

}

int main(){
    int num_list[5]={5,6,10,11,16}, temp[5];

    solve(21, 5, num_list, temp);


    return 0;
}