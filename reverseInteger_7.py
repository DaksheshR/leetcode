def reverse(x):
    sign = -1 if x<0 else 1
    x = x * sign
    r, n = 0, 0
    while(x):
        r = x % 10
        n = (10 * n) + r #n becomes reverse of x
        x = x // 10 #x becomes 0
    n = n * sign
    if(n < -(2**31) or n > (2**31)-1):
        return 0
    return(n)
