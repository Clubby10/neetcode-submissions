class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int maxProfit = 0;

        for (int r = 1; r < prices.size(); r++) {
            int profit = prices[r] - prices[l];
            maxProfit = max(maxProfit, profit);

            if (prices[l] > prices[r]) {
                l = r;
            }
        }

        return maxProfit;
    }
};
