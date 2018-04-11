# -------------------------------------------------------------------
#     File Name : Basic_Mathematics.py
#    Created By : GrinTwisted
#  Date Created : 1:25pm - 11 April 2018
#       Purpose : A collection of functions and algorithms common
#                 to basic mathematical calculations
#
#   Modified By : GrinTwisted
# Date Modified : 1:25pm - 11 April 2018
# -------------------------------------------------------------------

# Function : Factors
#  Purpose : Recursively finds and stores all factors of a number
#   Inputs : int n = The number your finding factors for a number
#            int f = The number your starting from to find a factor
#            set s = Set of numbers that are a factor of n
#  Outputs : Returns an ordered set of all factors of n
# Run Time : O(n log n)
def factors(n, f, s = set()):
    try:
        for i in range(f, n//f):
            if n % i == 0:
                s.update([i, n//i], factors2(n, i+1))
                break
    except:
        print("Error: Cannot Divide By 0")
    return sorted(s)