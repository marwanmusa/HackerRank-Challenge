"""
Task:
Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines.
If your array contains more than one modal value, choose the numerically smallest one.

Note:
Other than the modal value (which will always be an integer), your answers should be in decimal form,
rounded to a scale of 1 decimal place (i.e., 12.3, 7.0 format).
"""

N = int(input())
num_arr = list(map(int, input().split()))
num_arr.sort()

def mean(arr : list) -> int:
    mean_ = sum(arr)/len(arr)
    return mean_

def median(arr : list) -> int:
    mid = int(len(arr)/2)
    if len(arr) % 2 == 0:
        median_ = (arr[mid-1]+arr[mid])/2
    else:
        median_ = arr[mid]
    return median_

def unique(a : list) -> list:
    unique_list = []
    for i in a:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list    

def mode(arr : list) -> int:
    val = dict()
    for num in unique(arr):
        val[num] = 0
    for i in unique(arr):
        for j in arr:
            if i == j:
                val[i] += 1
    v = list(val.values())
    k = list(val.keys())
    return k[v.index(max(v))]

print(mean(num_arr))
print(median(num_arr))
print(mode(num_arr))