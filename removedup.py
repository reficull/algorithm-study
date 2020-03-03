def removeDup(nums):
    def rmNext(i,nums):
        if i+1 < len(nums)-1  and nums[i] == nums[i+1]:
            del nums[i+1]
        if i >= len(nums):
            return len(nums)
        return rmNext(i+1,nums)

    count = len(nums)
    for i in range(len(nums)):
        count = rmNext(i,nums)

    return count

arr = [0,0,1,1,1,2,2,3,3,4]
count = removeDup(arr)
print('count:',count)
print(arr)