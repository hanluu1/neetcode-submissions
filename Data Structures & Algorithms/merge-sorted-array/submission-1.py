class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #use pointers
        #one pointer at the last valid number of nums1 to swap number with pointer at the end of num 2
        i = m - 1
        #one at the end of nums1. this pointer is used to place the number in the position
        end = m + n - 1
        #one at the end of nums2
        j = n-1
        #because both array is already sorted so we compare the last element
        #in nums2 with the last element in nums1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[end] = nums1[i]
                i-=1
                
            else:
                nums1[end] = nums2[j]
                j-=1
            end-=1
            

        
        

        

