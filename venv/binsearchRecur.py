sortedarray = [1, 4, 6, 7, 9, 10, 15]

def binsearchRecur(sortedarray, target, left = 0, right = None):
    if right is None:
        right = len(sortedarray)-1

    # base case
    if left > right:
        return -1

    mid = (left + right) // 2

    if sortedarray[mid] == target:
        return mid

    if sortedarray[mid] > target:
        return binsearchRecur(sortedarray, target, left, mid-1)

    if sortedarray[mid] < target:
        return binsearchRecur(sortedarray, target, mid+1, right)


print(binsearchRecur(sortedarray, 10))
print(binsearchRecur(sortedarray, 130))