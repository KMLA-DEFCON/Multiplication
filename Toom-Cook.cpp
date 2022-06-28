#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int main(){
	long long int a,s,g,h;
	int d,a1,s1,cnt;
	long long a2[3],s2[3],f,t1,t2;
	long long a_0,a_1,a_m1,a_m2,a_inf;
	long long s_0,s_1,s_m1,s_m2,s_inf;
	long long r_0,r_1,r_m1,r_m2,r_inf;
	long long r0,r1,r2,r3,r4;
	cin >> a >> s;
	
	h=a;
	cnt=0;
	while(h>0){
		h/=10;
		cnt++;
	}
	a1=cnt/3;
	
	h=s;
	cnt=0;
	while(h>0){
		h/=10;
		cnt++;
	}
	s1=cnt/3;
	
	if(a1>s1){
		d=a1+1;
	}else{
		d=s1+1;
	}
	
	f=1;
	for(int i=0;i<d;i++){
		f*=10;
	}
	
	for(int i=0;i<3;i++){
		a2[i]=a%f;
		a/=f;
		s2[i]=s%f;
		s/=f;
	}
	
	t1=a2[0]+a2[2];
	a_0=a2[0];
	a_1=t1+a_1;
	a_m1=t1-a2[1];
	a_m2=2*(a_m1+a2[2])-a2[0];
	a_inf=a2[2];
	
	t2=s2[0]+s2[2];
	s_0=s2[0];
	s_1=t2+s_1;
	s_m1=t2-s2[1];
	s_m2=2*(s_m1+s2[2])-s2[0];
	s_inf=s2[2];
	
	r_0=a_0*s_0;
	r_1=a_1*s_1;
	r_m1=a_m1*s_m1;
	r_m2=a_m2*s_m2;
	r_inf=a_inf*s_inf;
	
	r0=r_0;
	r4=r_inf;
	r3=(r_m2-r_1)/3;
	r1=(r_1-r_m1)/2;
	r2=r_m1-r_0;
	r3=(r2-r3)/2+2*r_inf;
	r2=r2+r1-r_inf;
	r1=r1-r3;
	
	g=r0+r1*f+r2*f*f+r3*f*f*f+r4*f*f*f*f;
	cout << g;
	
    return 0;
}
