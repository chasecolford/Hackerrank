
import string
# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    return(" ".join(i.capitalize() for i in s))
    
