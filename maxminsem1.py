def findMinAndMax(nums):
 
    
    max = min = nums[0]
 
   
    for i in range(1, len(nums)):
 
        
        if nums[i] > max:
            max = nums[i]
 
        
        elif nums[i] < min:
            min = nums[i]
 
    print('The minimum element in the list is', min)
    print('The maximum element in the list is', max)
 
 
if _name_ == '_main_':
 
    nums = [5, 7, 2, 4, 9, 6]

       findMinAndMax(nums)
 
   
