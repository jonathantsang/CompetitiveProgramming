class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int leng = prices.size();
        int calc = 0;
        int start = prices[0];
        int possibleProfit = 0;
        int totalProfit = 0;
        for(int i = 0; i < leng; i++){
            // Possible profit
            possibleProfit = prices[i] - start - fee;
            
            // Adjust for -2
            if(i + 1 >= leng){
                    break;
            }
            calc = prices[i+1] - prices[i] + fee;
            
            // Previously negative
            if(calc < 0){
                // -2 for free
                int profit = prices[i] - start - fee;
                if(profit > 0){
                    cout << profit << " prof" << " sell at " << prices[i] << " buy at " << start;
                    totalProfit += profit;
                    
                }
                if(i + 1 >= leng){
                    break;
                }
                start = prices[i+1];
            }
        }
        if(possibleProfit > 0){
            totalProfit += possibleProfit;
        }
        return totalProfit;
    }
};