# Problem: Move Zeroes
#
# LeetCode: https://leetcode.com/problems/move-zeroes/

#
# Problem Statement:
# Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Constraints:
# 1) You must do this in-place (modify nums directly).
# 2) Try to minimize the number of operations.
#
# Example:
# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

#Burte force approach
# def move_zeroes_bruteforce1(nums):
#     non_zero = []
#     zeros = []

#     for num in nums:
#         if num == 0:
#             zeros.append(num)
#         else:
#             non_zero.append(num)

#     return non_zero + zeros

#time complexity = o(n)[loops through array once]
#space complexity = o(n)[extra space for the array declaration]
#another brutefore approach that changes the same list to pass the test case on leetcode
# def move_zeroes_bruteforce1(nums):

#     for num in nums:
#         if num == 0:
#             nums.append(0)
#             nums.remove(num)
#     return nums


#two pointer techniques used to solve the problem
#read pointer loops through array finding non zero numbers
#write pointer points to the index with element 0
#when read pointer finds the non zero number it swaps with the write pointer
#after swap both pointer moves forward
#[1,2,0,3,0,4,5] in this example, for each non zero number till 2 it swaps itself
#when read reaches the element 0, write pointer stay there but read pointer now moves 
#forward to find non zero number to swap
def move_zero_eff(nums):
    read_pointer = 0
    write_pointer = 0

    while ( read_pointer < len(nums)):
        if nums[read_pointer] != 0:
            nums[read_pointer], nums[write_pointer] = nums[write_pointer],nums[read_pointer] 
            write_pointer += 1
        read_pointer += 1
    return nums

print(move_zero_eff([1,2,3,0,4,5,0,6,7]))


