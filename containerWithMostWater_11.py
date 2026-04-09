def maxArea(height): #[1,8,6,2,5,4,8,3,7]
    l=0
    maxA = 0
    r=len(height)-1   # l = 0, r = 8
    while(l<r):
        length = min(height[l],height[r])
        width = r-l
        maxA = max(maxA, length*width)
        if(height[l] >= height[r]):
            r=r-1
        elif(height[l] < height[r]):
            l=l+1
    return(maxA)
