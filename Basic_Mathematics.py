# -------------------------------------------------------------------
#     File Name : Basic_Mathematics.py
#    Created By : GrinTwisted
#  Date Created : 1:25pm - 11 April 2018
#       Purpose : A collection of functions and algorithms common
#                 to basic mathematical calculations
#
#   Modified By : GrinTwisted
# Date Modified : 9:40pm - 13 April 2018
# -------------------------------------------------------------------

# Function : Factors
#  Purpose : Recursively finds and stores all factors of a number
#   Inputs : int n = The number your finding factors for a number
#            int f = The number your starting from to find a factor
#            set s = Set of numbers that are a factor of n
#  Outputs : Returns an ordered set of all factors of n
# Run Time : O(n log n)
def factors(n, f, s = set()):
    s.clear()
    try:
        if n == 1: s.update([1])
        for i in range(f, n//f+1):
            if n % i == 0:
                s.update([i, n//i], factors(n, i+1))
                break
    except:
        print("Error: Cannot Divide By 0")
    return sorted(s)


# Function : Euclids
#  Purpose : Finds the greatest common divisor of 2 numbers
#   Inputs : int a = The number your finding factors for a number
#            int b = The number your starting from to find a factor
#  Outputs : Returns the greatest common divisor as an integer
# Run Time : O(log(a + b))
def Euclids(a, b):
    if a < b: a, b = b, a
    if a % b == 0: return b
    else: return Euclids(b, a % b)