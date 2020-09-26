def isprime(N):
    factor = 0
    if(N > 1):
        if(N == 2):
            return True
        else:
            for value in range(2, N):
                if(N % value == 0):
                    factor = 1
    else:
        return False
    if(factor == 0):
        return True
    else:
        return False