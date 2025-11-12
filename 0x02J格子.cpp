#include<stdio.h>
int main(){
    int T;
    scanf("%d",&T);
    while(T>0){
        T--;
        long long n,m,k,max,min;
        scanf("%lld %lld %lld",&n,&m,&k);
        if(m>n){
            min=n;max=m;
        }else{
            min=m;max=n;
        }
        
        if(k>min&&k>1){
            printf("0\n"); 
        }else if(k==1){
            printf("1\n");
        }else{
            long long x,y,x1,y1,t1,t2;
            x=1;
			y=1;
			t1=min;
			t2=max;
            for(int i=0;i<k;i++){
                x*=t2;
                t2--;
            }
            for(int j=0;j<k;j++){
                	x*=t1;
                	t1--;
				}
			long long t3=max*min;
            for(int s=0;s<k;s++){
                y*=t3;
                t3--;
            }
            x1=x;
            y1=y;
            while(y1!=0){
                long long r=x1%y1;
                x1=y1;
                y1=r;
            }
            x/=x1;
            y/=x1;
            printf("%lld/%lld\n",x,y);
        }
    }
    return 0;
}
