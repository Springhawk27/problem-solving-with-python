#  sum of array

def arraySum(array):
    sum = 0
    for i in array:
        sum = sum + i
    return sum


arr = [1, 2, 3, 4, 5]
result = arraySum(arr)
print("Sum of the given array {} is {}".format(arr, result))
