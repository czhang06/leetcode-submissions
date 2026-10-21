function maxProfit(prices: number[]): number {
    let result = 0;

    let msf = 10**4 + 1

    for (let i = 0; i < prices.length; i++) {
        if (prices[i] < msf) {
            msf = prices[i]
        } else {
            result = Math.max(result, prices[i] - msf)
        }
    }

    return result
    
};