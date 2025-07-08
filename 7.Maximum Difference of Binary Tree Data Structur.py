def maximum_num_ele(arr):
    arr=sorted(arr)
    size=len(arr)
    maximum_def= - 9999*999

    for i in range(size-1):
        if (arr[i+1]-arr[i] > maximum_def):
            maximum_def=arr[i+1] - arr[i]
    return maximum_def
    
arr=[5,32,45,4,12,18,25,50,70]
print(arr)
print("THiS is the maximum number of array",maximum_num_ele(arr))