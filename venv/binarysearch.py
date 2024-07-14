sortedarr = [1, 4, 6, 7, 9, 10, 15]

def binarysearch(sortedarr, target):
    left = 0
    right = len(sortedarr) - 1

    while(left<=right):
        mid = (left + right) // 2
        if sortedarr[mid] == target:
            return mid
        if sortedarr[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return -1

print(binarysearch(sortedarr, 10))
print(binarysearch(sortedarr, 0))
