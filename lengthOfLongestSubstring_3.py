def lengthOfLongestSubstring(s: str) -> int:
    leng = 0
    le = []
    d = {}
    for i in range(len(s)-1):
        d[i] = s[i]
        if(s[i] in d):
            leng = len(d)
            le.append(leng)
            leng = 0
            d = {}            
    return(max(le))