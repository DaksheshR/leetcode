def RTI(s):
    def strToInt(c):
        if(c == 'I'):
            return(1)
        elif(c == 'V'):
            return(5)
        elif(c == 'X'):
            return(10)
        elif(c == 'L'):
            return(50)
        elif(c == 'C'):
            return(100)
        elif(c == 'D'):
            return(500)
        elif(c == 'M'):
            return(1000)
    sum_num = 0
    for i in range(len(s)):
        if(i+1 < len(s) and strToInt(s[i]) < strToInt(s[i+1])):
            sum_num = sum_num - strToInt(s[i])
        else:
            sum_num = sum_num + strToInt(s[i])

    return(sum_num)
        
