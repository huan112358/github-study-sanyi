#include <stdio.h>
#include <math.h>
int main(){
    int T;
    scanf("%d",&T);
    while(T>0){
        T--;
        int x1,y1,r1,x2,y2,r2;
        scanf("%d %d %d",&x1,&y1,&r1);
        scanf("%d %d %d",&x2,&y2,&r2);
        long long s=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
        long long l=sqrt(s);
        int t=0;
        if(r1>r2){
            t=r1-r2;
        }else{
            t=r2-r1;
        }
        if(l<t){
            printf("1\n");
        }else if(l=t){
            printf("2\n");
        }else if(l>t&&l<r1+r2){
            printf("3\n");
        }else if(l==r1+r2){
            printf("4\n");
        }else if(l>r1+r2){
            printf("5\n");
        }
    }
    return 0;
}
             
