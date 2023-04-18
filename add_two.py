# import time

# startone = time.time()
# def twoSum(nums, target):
#     results = [(n ,j) if n != j and nums[n]+ nums[j] == target else None
#         for n in range(len(nums))
#         for j in range(len(nums))]

#     none_indexing = results.index(next(filter(lambda x: x is not None, iter(results))))
    
#     return results[none_indexing]

# endone = time.time()

# print("The 1st time of execution of above program is :",
#       (endone-startone) * 10**3, "ms")

# starttwo = time.time()
# def sumys(nums, target):
#     for n in range(len(nums)):
#         for j in range(len(nums)):
#             if n != j and nums[n] + nums[j] == target:
#                 return n, j
# # print(twoSum([3,2,4], 6))
# endtwo = time.time()
# print("The 2nd time of execution of above program is :",
#       (endtwo-starttwo) * 10**3, "ms")

# startthree = time.time()

def asum( nums, target):
        results = [(i, j) for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i] + nums[j] == target]
        return results[0]
print(asum([3,2,4], 6))

# endthree = time.time()
# print("The 3rd time of execution of above program is :",
#       (endthree-startthree) * 10**3, "ms")