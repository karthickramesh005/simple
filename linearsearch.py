
def linearsearch(arr,k):
    n = len(arr)
    

    for i in range(n):
        if arr[i] == k :
            return i
        
    return -1
        
        
    
    
arr = list(map(int,input("Enter a aray elements : ").split()))
k = int(input("Enter a finding element : "))
print(linearsearch(arr,k))
