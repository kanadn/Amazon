import heapq

def getMaxStability(reliability, availability):
    MOD = 1000000007
    n = len(reliability)

    servers = [(a, r) for a, r in zip(availability, reliability)]
    #servers.sort()
    max_stability = 0
    
    def backtrack(i, minAvailability, relibilitySum, currStability):
        if i == n:
            nonlocal max_stability
            max_stability = max(max_stability, currStability)
            return
        
        # All subsets of servers that include the current server
        newMinAvailability = min(minAvailability, servers[i][0])
        newRelibilitySum = relibilitySum + servers[i][1]
        newCurrStability = (newRelibilitySum * newMinAvailability) % MOD
        backtrack(i + 1, newMinAvailability, newRelibilitySum, newCurrStability)

        # All subsets of servers that exclude the current server
        backtrack(i + 1, minAvailability, relibilitySum, currStability)
    
    backtrack(0, float('inf'), 0, 0)



    return max_stability


test_cases = [
    {
        "name": "Test Case 1: Single Server – Normal Case",
        "reliability": [5],
        "availability": [10],
        "expected": 50
    },
    {
        "name": "Test Case 2: Single Server with Zero Reliability",
        "reliability": [0],
        "availability": [10],
        "expected": 0
    },
    {
        "name": "Test Case 3: Single Server with Zero Availability",
        "reliability": [10],
        "availability": [0],
        "expected": 0
    },
    {
        "name": "Test Case 4: Two Servers – Combination Improves the Result",
        "reliability": [1, 10],
        "availability": [10, 1],
        "expected": 11
    },
    {
        "name": "Test Case 5: Provided Example",
        "reliability": [1, 2, 2],
        "availability": [1, 1, 3],
        "expected": 6
    },
    {
        "name": "Test Case 6: All Servers with Identical Values",
        "reliability": [5, 5, 5, 5],
        "availability": [5, 5, 5, 5],
        "expected": 100
    },
    {
        "name": "Test Case 7: Multiple Servers – Same Availability, Varying Reliability",
        "reliability": [3, 4, 5],
        "availability": [2, 2, 2],
        "expected": 24
    },
    {
        "name": "Test Case 8: One Server Dominates",
        "reliability": [1000, 2, 3],
        "availability": [1000, 2, 3],
        "expected": 1000000
    },
    {
        "name": "Test Case 9: Maximum Values to Test Modulo Arithmetic",
        "reliability": [1000000006, 1000000006, 1000000006],
        "availability": [1000000006, 1000000006, 1000000006],
        "expected": 3
    },
    {
        "name": "Test Case 10: Mixed Values with a Non-Obvious Best Subset",
        "reliability": [3, 2, 5, 7],
        "availability": [4, 6, 2, 5],
        "expected": 48
    },
    {
        "name": "Test Case 11: More Servers with Varying Factors",
        "reliability": [10, 5, 10, 5],
        "availability": [3, 4, 2, 8],
        "expected": 60
    },
    {
        "name": "Test Case 12: Three Servers with Contrasting Values",
        "reliability": [10, 1, 10],
        "availability": [1, 10, 1],
        "expected": 21
    }
]

# Example testing function
def run_tests(func):
    for tc in test_cases:
        result = func(tc["reliability"], tc["availability"])
        status = "PASS" if result == tc["expected"] else "FAIL"
        print(f'{tc["name"]}: {status} (Expected: {tc["expected"]}, Got: {result})')

# Example: Replace getMaxStability with your function name
# run_tests(getMaxStability)
run_tests(getMaxStability)