import java.util.*;
class Ls{
	public static void main(String[] args){
int a[]={1,2,3,5,6,8,7};
int smallest=a[0],largest=a[0],i=1;
int m=a.length;
while(i<m){
	 if(a[i]<smallest)
	 {
		 smallest=a[i];
	 }
	 if(a[i]>largest)
	 {
		 largest=a[i];
	 }
	 i++;

	}
	System.out.println(smallest+" "+largest);
	int range=largest-smallest;
	System.out.println(range);
}
}

		 