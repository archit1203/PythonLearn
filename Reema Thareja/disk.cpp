#include <iostream.h>
using namespace std;

int main(){
    int i , n , req[50],mov,cp;
    cout<<"Enter the current position"<<endl;
    cin>>cp;
    cout<<"Enter the number of requests"<<endl;
    cin>>n;
    cout<<"Enter the request order"<<endl;
    for(int i=0;i<n;i++){
        cin>>req[i];
    }
    mov=mov+(cp-req[0]);
    cout<<cp<<" -> "<<req[0]<<endl;
    for(i=0;i<n;i++){
        mov=mov+(req[i]-req[i-1]);
        cout<<"-> "<<req[i]<<endl;
    }
    cout<<"\n";
    cout<<"Total mov = "<<mov<<endl;
}