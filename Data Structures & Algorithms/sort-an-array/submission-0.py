class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr,l, mid, r):
            left, right = arr[l:mid+1], arr[mid+1:r+1]
            i, j, k = l , 0, 0
            #while left and right in bound use two pointer to merge
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else: 
                    arr[i] = right[k]
                    k+=1
                i+=1
            #if either left and right out of bound first
            while j < len(left):
                nums[i] = left[j]
                j+=1
                i+=1
            while k < len(right):
                nums[i] = right[k]
                k+=1
                i+=1
            
        #merge sort
        def mergeSort(arr, l, r):
            if l == r:
                return arr
            n = (l+r) //2
            mergeSort(arr,l,n)
            mergeSort(arr,n+1,r)
            merge(arr,l,n,r)
            return arr
        return mergeSort(nums, 0, len(nums)-1)
