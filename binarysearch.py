def binarysearch(arr,k):
    n = len(arr)
    l = arr[0]
    r = arr[-1]

    for i in range(n):
        m = l + (r - l) / 2
        if arr[i] == k :
            return i
        
    return -1
        
        
    
    
arr = list(map(int,input("Enter a aray elements : ").split()))
k = int(input("Enter a finding element : "))
print(binarysearch(arr,k))
