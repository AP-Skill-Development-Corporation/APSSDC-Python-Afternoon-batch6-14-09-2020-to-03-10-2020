#Program for find the factorial of number in given range
def fact1(N):
    f = 1
    for value in range(1,N+1):
        f = f*value
    return f



#Function to which checks the given string is palindrome or not

def ispalindrome(s):
    if (s==s[::-1]):
        return True
    else:
        return False