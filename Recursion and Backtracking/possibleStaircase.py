"""
A child is running up a staircase with N steps, and can hop either 1 step,
2 steps or 3 steps at a time. Implement a method to count how many possible 
ways the child can run up to the stairs. You need to return number of possible ways W.
Input n = 4
Output n = 7
"""
def possibleStair(n):
    if(n < 3):
        return n
    if(n==3):
        return 4
    return possibleStair(n-1) + possibleStair(n-2) + possibleStair(n-3)



print(possibleStair(4))