
def twoSum(nums, target):
    #create a dictionary to store the values and their positions
    d = {}
    for x, y in enumerate(nums):
        if target - y in d:
            return [d[target - y], x]
        d[y] = x
    return []
        
print(twoSum([2,7,11,15], 9))

    