#include <iostream>
using namespace std;

struct coin_number{
    int number;
    int data;
    coin_number* next;
};


coin_number* coin(int n, int coins[], int amount){
    coin_number* head = new coin_number();
    head->next = NULL;
    head->number = 0;
    coin_number* help = head;
    int i=0;
    while(i != n){
        help->data = coins[i];
        if(amount == 0)return head;
        if(coins[i] <= amount){
            amount-=coins[i];
            help->number+=1;
        }
        else{
            coin_number* temp = new coin_number();
            temp->next = NULL;
            temp->number = 0;
            help->next = temp;
            help = temp;
            i++;
        }

    }
    return NULL;

}

int main(){
    int n, amount;
    cin>>n;
    cin>>amount;
    int coin_list[n];

    for(int i=0; i<n; i++)cin>>coin_list[i];
    coin_number* result = coin(n, coin_list, amount);
    if(result == NULL)cout<<-1;
    else {
        cout<<"coin"<<"\t"<<"number"<<endl;
        while (result != NULL) {
            cout<<result->data<<"\t"<<result->number<<endl;
            result = result->next;
        }
    }
    return 0;
}