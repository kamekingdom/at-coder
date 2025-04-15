def minimal_expected_cost(N, A, X, Y):
    import sys
    sys.setrecursionlimit(100000)
    from functools import lru_cache
    
    # Memoize the expected costs
    @lru_cache(None)
    def dp(n):
        if n == 0:
            return 0  # Base case, no cost if n is already 0
        
        # Cost for the deterministic operation (dividing by A)
        cost1 = X + dp(n // A)
        
        # Cost for the stochastic operation (rolling a die)
        cost2 = Y
        for b in range(1, 7):  # Possible die outcomes
            cost2 += dp(n // b) / 6
        
        return min(cost1, cost2)
    
    # Calculate the minimum expected cost starting from N
    result = dp(N)
    
    return result

# Example Inputs from the problem description
inputs = [
    (3, 2, 10, 20),
    (3, 2, 20, 20),
    (314159265358979323, 4, 223606797, 173205080)
]

# Results for each input
results = [minimal_expected_cost(*inp) for inp in inputs]
print(results)
