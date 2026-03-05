def myAtoi(s):
    if not (len(s)>=0 and len(s)<=200):
        return(0)
    s = s.lstrip() #leading spaces are taken now check sign
    if not s:
        return(0)
    NegSign = False #positive
    i = 0
    num = 0
    if(s[i] in ['+','-']): #first char
        NegSign = True if s[i] == '-' else False
        i = i+1
    while(i<len(s) and s[i].isdigit()):
        num = num*10 + int(s[i])
        i = i+1
    if(NegSign):
        num = -num
    if(num<-2**31):
        return(-2**31)
    if(num>2**31-1):
        return(2**31-1)
    return(num) 
