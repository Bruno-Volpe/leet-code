
def findMaximumGreatness(arr):
    sorted_arr = sorted(arr)
    greatness = 0
    for i in range(len(arr)):
        for j in range(len(sorted_arr)):
            if sorted_arr[j] > arr[i]:
                arr[i] = sorted_arr.pop(j)
                greatness += 1
                break
    return greatness
