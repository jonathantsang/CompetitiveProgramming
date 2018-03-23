class Solution {
public:
    int minSwap(vector<int>& a, vector<int>& b) {
      int x=0,y=1;
      int N=a.size();
      for(int i=1;i<N;i++){
		int X=1e9,Y=1e9;
        cout << x << " " << y << endl;
		if(a[i]>a[i-1] && b[i]>b[i-1]){
	  		X=min(X,x);
	  		Y=min(Y,y+1);
		}
		if(a[i]>b[i-1] && b[i]>a[i-1]){
	  		X=min(X,y);
	  		Y=min(Y,x+1);
		}
		x=X,y=Y;
      }
      return min(x,y);
	}
};