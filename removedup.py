def removeDup(nums):
    def rmNext(i,nums):
        if i+1 < len(nums)-1  and nums[i] == nums[i+1]:
            del nums[i+1]
            i = max(i-1,0) 
        if i+1 >= len(nums):
            return len(nums)
        return rmNext(i+1,nums)

    count = len(nums)
    count = rmNext(0,nums)

    return count

arr = [0,0,1,1,1,2,2,3,3,4]
count = removeDup(arr)
print('count:',count)
print(arr)
