a = [2, 6, 4, 8, 6, 9, 1]

def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


print(bubblesort(a))