def solve(arr):
    # this is the dutch flag apraoch for the the airpo check pint cod e
    low , mid ,high =0,0,len(arr)-1
    while mid <= high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
            # mid+=1
    return arr
n=int(input("Enter the number of element="))
arr=list(map(int,input("Enter the risks factor for each checkppints (0=low,1=mid,2=high=)").split()))
sorted_risks = solve(arr)
print("Sorted risk levels:", sorted_risks)
    