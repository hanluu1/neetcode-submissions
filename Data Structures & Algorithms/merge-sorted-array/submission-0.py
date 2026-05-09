class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #use pointers
        #one pointer at m - 1
        i = m-1
        #one at the end of nums1
        j = len(nums1) - 1 #=m+n -1
        #one at the end of nums2
        k = len(nums2) - 1
        #because both array is already sorted so we compare the last element
        #in nums 2 with the last element in nums1
        #if nums2[k] > nums1[i] then it is place the end if not then it place at the position
        #of nums1[i] and i have to move to the next empty space
        while k >= 0:
            if i >=0 and nums1[i] > nums2[k]:
                nums1[j] = nums1[i]
                i-=1
            else:
                nums1[j] = nums2[k]
                k-=1
            j-=1


        

