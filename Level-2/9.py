nums= [7, 2, 5, 1, 9, 3]
try:
    for i in range(len(nums)+1):
        print(nums[i])
except IndexError:
    print("Index out of range")
    