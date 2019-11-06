n = input()
nums = {}
for i in n.split():
    nums[i]= nums.get(i,0) + 1
del nums["0"]
minn = next(iter(nums))
for i in nums:
    a = int(nums.get(i))
    if a == nums.get(minn):
        if nums[i] > nums[minn]:
            minn = i
    else:
        if a < nums.get(minn):
            minn = i
print(minn)
