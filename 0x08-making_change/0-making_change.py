#!/usr/bin/python3
"""Change making module.
"""

def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
                                
    """Initialize dp array where dp[i] means the fewest number of coins for total i"""
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins are needed for total 0
                                            
    """Compute the fewest coins for each total from 1 to total"""
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
                                                                                    
    """If dp[total] is still infinity, that means it's not possible to make the total"""
    return dp[total] if dp[total] != float('inf') else -1

