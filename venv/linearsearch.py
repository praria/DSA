arr = [3, 5, 8, 1, 0, 4]

def linearsearch(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
        return -1

print(linearsearch(arr, 3))